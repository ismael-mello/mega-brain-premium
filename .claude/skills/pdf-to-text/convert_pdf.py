#!/usr/bin/env python3
"""
PDF to Text Converter - Mega Brain
Converte PDF para texto puro usando PyMuPDF.
Uso: python convert_pdf.py <caminho_do_pdf> [--output txt|md] [--pages 1-5]
"""

import sys
import json
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print(json.dumps({"error": "PyMuPDF not installed. Run: pip install pymupdf"}))
    sys.exit(1)


def convert_pdf(pdf_path: str, output_format: str = "txt", page_range: str = None) -> dict:
    """Convert PDF to text or markdown."""
    path = Path(pdf_path)
    if not path.exists():
        return {"error": f"File not found: {pdf_path}"}
    if path.suffix.lower() != ".pdf":
        return {"error": f"Not a PDF file: {pdf_path}"}

    doc = fitz.open(str(path))
    total_pages = len(doc)

    # Parse page range
    start, end = 0, total_pages
    if page_range:
        parts = page_range.split("-")
        start = max(0, int(parts[0]) - 1)
        end = min(total_pages, int(parts[-1])) if len(parts) > 1 else start + 1

    lines = []
    for page_num in range(start, end):
        page = doc[page_num]
        text = page.get_text("text")

        if output_format == "md":
            lines.append(f"\n## Page {page_num + 1}\n")

        lines.append(text)

    doc.close()

    content = "\n".join(lines).strip()

    # Save output
    ext = ".md" if output_format == "md" else ".txt"
    output_path = path.with_suffix(ext)
    output_path.write_text(content, encoding="utf-8")

    return {
        "success": True,
        "input": str(path),
        "output": str(output_path),
        "total_pages": total_pages,
        "pages_converted": f"{start+1}-{end}",
        "chars": len(content),
        "lines": content.count("\n") + 1,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_pdf.py <pdf_path> [--output txt|md] [--pages 1-5]")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_format = "txt"
    page_range = None

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_format = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--pages" and i + 1 < len(sys.argv):
            page_range = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    result = convert_pdf(pdf_path, output_format, page_range)
    print(json.dumps(result, indent=2, ensure_ascii=False))
