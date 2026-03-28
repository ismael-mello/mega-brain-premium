# Meta Ads Marketing API — Documentacao Tecnica Completa

**Versao da API:** v25.0 (atual)
**Base URL:** `https://graph.facebook.com/v25.0/`
**Data da pesquisa:** 2026-03-28
**Fontes:** 20 paginas oficiais (developers.facebook.com) + guias especializados

---

## TL;DR

A Meta Marketing API e uma colecao de endpoints Graph API para gerenciar campanhas publicitarias no Facebook, Instagram, Messenger e WhatsApp. Estrutura hierarquica: **Campaign > Ad Set > Ad Creative > Ad**. Suporta CRUD completo, targeting avancado (Custom/Lookalike Audiences), reporting com 30+ metricas e breakdowns, Conversions API (CAPI) para tracking server-side, e sistema robusto de rate limiting baseado em pontos (BUC).

---

## 1. Estrutura de Campanhas (Campaign Hierarchy)

### Hierarquia de Objetos

```
Ad Account (act_{ID})
  └── Campaign (objetivo)
        └── Ad Set (budget, targeting, schedule)
              └── Ad (creative + placement)
                    └── Ad Creative (visual/copy)
```

### 1.1 Campaign API

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/campaigns`

| Campo | Tipo | Obrigatorio | Descricao |
|-------|------|-------------|-----------|
| name | string | Sim | Nome da campanha |
| objective | enum | Sim | OUTCOME_AWARENESS, OUTCOME_TRAFFIC, OUTCOME_ENGAGEMENT, OUTCOME_LEADS, OUTCOME_APP_PROMOTION, OUTCOME_SALES |
| status | enum | Sim | ACTIVE, PAUSED |
| special_ad_categories | array | Sim | HOUSING, EMPLOYMENT, CREDIT, ISSUES_ELECTIONS_POLITICS, ou [] |

**CRUD Operations:**
```bash
# CREATE
POST /act_{AD_ACCOUNT_ID}/campaigns
  name=MinhaCampanha&objective=OUTCOME_SALES&status=PAUSED

# READ
GET /{CAMPAIGN_ID}?fields=name,objective,status,daily_budget

# READ ALL (account level)
GET /act_{AD_ACCOUNT_ID}/campaigns?fields=name,status

# UPDATE
POST /{CAMPAIGN_ID}
  name=NovoNome&status=ACTIVE

# DELETE
DELETE /{CAMPAIGN_ID}
```

**Status values:** ACTIVE, PAUSED, DELETED

---

### 1.2 Ad Set API

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/adsets`

| Campo | Tipo | Obrigatorio | Descricao |
|-------|------|-------------|-----------|
| name | string | Sim | Nome do ad set |
| campaign_id | string | Sim | ID da campanha pai |
| targeting | object | Sim | Especificacao de targeting |
| daily_budget / lifetime_budget | int | Sim (um dos dois) | Orcamento em centavos |
| start_time | datetime | Sim | Inicio (ISO 8601) |
| end_time | datetime | Condicional | Obrigatorio com lifetime_budget |
| billing_event | enum | Sim | IMPRESSIONS, CLICKS, ACTIONS |
| optimization_goal | enum | Sim | REACH, IMPRESSIONS, LINK_CLICKS, CONVERSIONS, etc. |
| status | enum | Sim | ACTIVE, PAUSED |

**Budget:** Valores em centavos (e.g., R$50.00 = 5000)

**Status fields:**
- `status` — usado em criacao/update
- `configured_status` — status configurado pelo anunciante (leitura)
- `effective_status` — status efetivo considerando campanha pai (leitura)

```bash
# CREATE
POST /act_{AD_ACCOUNT_ID}/adsets
  name=MeuAdSet
  &campaign_id={CAMPAIGN_ID}
  &daily_budget=5000
  &billing_event=IMPRESSIONS
  &optimization_goal=LINK_CLICKS
  &targeting={"geo_locations":{"countries":["BR"]}}
  &start_time=2026-04-01T00:00:00-0300
  &status=PAUSED

# READ ad sets de uma campanha
GET /{CAMPAIGN_ID}/adsets?fields=name,daily_budget,targeting,status
```

---

### 1.3 Ad Creative API

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/adcreatives`

| Campo | Tipo | Descricao |
|-------|------|-----------|
| name | string | Nome do creative |
| object_story_spec | object | Conteudo do anuncio (imagem, video, carrossel) |
| image_hash | string | Hash da imagem enviada |
| video_data | object | Dados do video |
| url_tags | string | UTM parameters |

**IMPORTANTE:** Ad Creatives **NAO podem ser modificados** apos criacao. Para alterar, crie um novo creative.

```bash
# CREATE
POST /act_{AD_ACCOUNT_ID}/adcreatives
  name=MeuCreative
  &object_story_spec={...}

# READ
GET /{CREATIVE_ID}?fields=name,object_story_spec,thumbnail_url
```

---

### 1.4 Ad (Individual)

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/ads`

| Campo | Tipo | Obrigatorio | Descricao |
|-------|------|-------------|-----------|
| name | string | Sim | Nome do anuncio |
| adset_id | string | Sim | ID do ad set pai |
| creative | object | Sim | `{"creative_id": "{CREATIVE_ID}"}` |
| status | enum | Sim | ACTIVE, PAUSED |

```bash
# CREATE
POST /act_{AD_ACCOUNT_ID}/ads
  name=MeuAnuncio
  &adset_id={ADSET_ID}
  &creative={"creative_id":"{CREATIVE_ID}"}
  &status=PAUSED
```

---

## 2. Targeting & Audiences

### 2.1 Custom Audiences

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/customaudiences`

**Tipos de fonte:**
- `USER_PROVIDED_ONLY` — dados fornecidos pelo anunciante
- `PARTNER_PROVIDED_ONLY` — dados de parceiros
- `BOTH_USER_AND_PARTNER_PROVIDED` — ambos

**Schema de dados do usuario (14+ campos):**

| Campo | Hashing | Descricao |
|-------|---------|-----------|
| EMAIL | SHA256 | Email normalizado (lowercase, trim) |
| PHONE | SHA256 | Telefone com codigo pais (+5511...) |
| FN | SHA256 | Primeiro nome (lowercase) |
| LN | SHA256 | Sobrenome (lowercase) |
| GEN | SHA256 | Genero (m/f) |
| DOBY/DOBM/DOBD | SHA256 | Ano/mes/dia nascimento |
| CT | SHA256 | Cidade |
| ST | SHA256 | Estado |
| ZIP | SHA256 | CEP |
| COUNTRY | SHA256 | Pais (2 letras ISO) |
| FI | SHA256 | Inicial do nome |
| EXTERN_ID | NAO hash | ID externo |
| MADID | NAO hash | Mobile Advertiser ID |

```bash
# CRIAR audience
POST /act_{AD_ACCOUNT_ID}/customaudiences
  name=MeusClientes
  &subtype=CUSTOM
  &customer_file_source=USER_PROVIDED_ONLY

# UPLOAD usuarios (max 10K por batch)
POST /{AUDIENCE_ID}/users
{
  "session": {
    "session_id": 123456,
    "batch_seq": 1,
    "last_batch_flag": true,
    "estimated_num_total": 5000
  },
  "payload": {
    "schema": ["EMAIL", "FN", "LN"],
    "data": [
      ["<SHA256_EMAIL>", "<SHA256_FN>", "<SHA256_LN>"]
    ]
  }
}

# REMOVER usuarios
DELETE /{AUDIENCE_ID}/users
{
  "schema": "EMAIL_SHA256",
  "data": ["<HASH1>", "<HASH2>"]
}

# REMOVER de TODAS as audiences
DELETE /act_{AD_ACCOUNT_ID}/usersofanyaudience
```

**Limites por conta:**
- 500 file audiences standard
- 10,000 website custom audiences
- 200 mobile app audiences
- 500 lookalike audiences

**Retencao:** Audiences sem uso por 2+ anos sao marcadas para delecao automatica.

---

### 2.2 Lookalike Audiences

**Endpoint:** `POST /act_{AD_ACCOUNT_ID}/customaudiences`

**Requisitos:** Minimo 100 membros na audience semente (200+ recomendado).

```bash
POST /act_{AD_ACCOUNT_ID}/customaudiences
{
  "name": "Lookalike BR 1%",
  "subtype": "LOOKALIKE",
  "origin_audience_id": "{CUSTOM_AUDIENCE_ID}",
  "lookalike_spec": {
    "type": "similarity",
    "ratio": 0.01,
    "country": "BR"
  }
}
```

**Parametros lookalike_spec:**
| Parametro | Valores | Descricao |
|-----------|---------|-----------|
| type | similarity / reach | Top 1% vs Top 5% |
| ratio | 0.01 - 0.20 | Tamanho relativo (1% a 20%) |
| country | ISO 2-letter | Pais alvo |
| starting_ratio | 0.01+ | Para ranges (ex: 0.03 a 0.05) |

**Nota:** O parametro `country` no lookalike_spec esta **deprecated**. Defina a localizacao no targeting do Ad Set.

---

### 2.3 Detailed Targeting

**Endpoints de descoberta:**

```bash
# BUSCAR interesses/comportamentos
GET /act_{AD_ACCOUNT_ID}/targetingsearch
  ?q=fitness&limit_type=interests

# SUGESTOES baseadas em targeting existente
GET /act_{AD_ACCOUNT_ID}/targetingsuggestions
  ?targeting_list=[{"type":"interests","id":6003283735711}]

# NAVEGAR hierarquia
GET /act_{AD_ACCOUNT_ID}/targetingbrowse

# VALIDAR targeting
GET /act_{AD_ACCOUNT_ID}/targetingvalidation
  ?targeting_list=[{"type":"interests","id":6003283735711}]
```

**limit_type values:** interests, behaviors, education_schools, education_majors, work_positions, work_employers, income, life_events, industries, family_statuses

**Resposta:**
```json
{
  "id": "6003283735711",
  "name": "Fitness",
  "audience_size_lower_bound": 450000000,
  "audience_size_upper_bound": 500000000,
  "path": ["Interests", "Sports and outdoors", "Fitness"],
  "valid": true
}
```

---

### 2.4 Reach Estimation

```bash
GET /act_{AD_ACCOUNT_ID}/reachestimate?targeting_spec={...}
GET /act_{AD_ACCOUNT_ID}/delivery_estimate?targeting_spec={...}
```

**Nota:** Retorna `-1` ate a campanha ser publicada. Audiences inativas (90+ dias) tambem retornam `-1`.

---

## 3. Insights & Reporting API

### 3.1 Endpoints

```bash
# Account level
GET /act_{AD_ACCOUNT_ID}/insights?fields=impressions,spend,reach

# Campaign level
GET /{CAMPAIGN_ID}/insights?fields=impressions,spend,actions

# Ad Set level
GET /{ADSET_ID}/insights?fields=impressions,clicks,cpm

# Ad level
GET /{AD_ID}/insights?fields=impressions,spend,actions
```

### 3.2 Metricas Principais

| Metrica | Descricao |
|---------|-----------|
| impressions | Total de impressoes |
| reach | Pessoas unicas alcancadas |
| clicks | Todos os cliques |
| link_clicks | Cliques no link |
| spend | Gasto total |
| actions | Acoes (purchase, lead, etc.) |
| cost_per_action_type | Custo por tipo de acao |
| unique_clicks | Cliques unicos |
| cpm | Custo por mil impressoes |
| frequency | Media de vezes que cada pessoa viu |
| cost_per_reach | Custo por pessoa alcancada |
| total_actions | Total de acoes |

### 3.3 Breakdowns

**Demograficos:** age, gender
**Plataforma:** publisher_platform, device_platform, impression_device, platform_position
**Geograficos:** country, region, dma
**Creative Assets:** image_asset, video_asset, body_asset, title_asset
**Acao:** action_type, action_device, action_destination
**Produto:** product_id
**Temporal:** hourly_stats_aggregated_by_advertiser_time_zone

```bash
# Breakdown por idade e genero
GET /{CAMPAIGN_ID}/insights
  ?fields=impressions,spend
  &breakdowns=age,gender
  &date_preset=last_7d
```

**Combinacoes incompativeis:**
- `unique_*`, `reach`, `frequency` NAO funcionam com breakdowns hourly
- `app_store_clicks`, `relevance_score` NAO funcionam com nenhum breakdown

### 3.4 Date Presets & Time Ranges

**Presets:** last_7d, last_28d, lifetime

**Custom:**
```bash
&time_range={"since":"2026-03-01","until":"2026-03-28"}
```

### 3.5 Attribution Windows

| Window | Descricao |
|--------|-----------|
| 1d_click | 1 dia apos clique |
| 1d_view | 1 dia apos visualizacao |
| 7d_click | 7 dias apos clique (DEFAULT) |
| 28d_click | 28 dias apos clique |
| 28d_view | 28 dias apos visualizacao |

```bash
&action_attribution_windows=['1d_click','7d_click']
```

**Mudanca importante (Junho 2025):** `use_unified_attribution_setting` e `action_report_time` foram **deprecated**. Attribution agora alinha automaticamente com as configuracoes do Ads Manager.

### 3.6 Filtering & Sorting

```bash
# Filtrar por status
&filtering=[{"field":"ad.effective_status","operator":"IN","value":["ACTIVE","PAUSED"]}]

# Filtrar por label
&filtering=[{"field":"ad.adlabels","operator":"ANY","value":["Remarketing"]}]

# Ordenar por alcance (decrescente)
&sort=reach_descending

# Agregar por nivel
&level=ad  # Quebra metricas da campanha por ad individual
```

### 3.7 Async Reports (para grandes volumes)

```bash
# Criar job async
POST /{AD_OBJECT_ID}/insights
  ?fields=impressions,spend,actions
  &breakdowns=age,gender
  &date_preset=last_28d
  &level=ad

# Resposta: job ID
# Polling ate conclusao (pode levar ate 1 hora)
GET /{JOB_ID}
```

**Performance:**
- Dados atualizam a cada **15 minutos**
- Dados nao mudam apos **28 dias**
- Metricas `unique_*` sao resource-intensive
- Para grandes extractions, use **async** (mais lento mas confiavel)

### 3.8 Paginacao

Cursor-based:
```json
{
  "paging": {
    "cursors": {
      "before": "MAZDZD",
      "after": "MQZDZD"
    }
  }
}
```

---

## 4. Conversions API (CAPI)

### 4.1 Visao Geral

O CAPI conecta dados de marketing do servidor do anunciante diretamente aos sistemas Meta, complementando o Facebook Pixel (browser-side). Permite tracking server-side robusto, independente de cookies/ad blockers.

**Endpoint:** `POST https://graph.facebook.com/{API_VERSION}/{PIXEL_ID}/events`

### 4.2 Payload de Evento

```json
{
  "data": [{
    "event_name": "Purchase",
    "event_time": 1764975551,
    "event_source_url": "https://exemplo.com/checkout",
    "action_source": "website",
    "event_id": "nonce_abc123",
    "user_data": {
      "em": "<SHA256_EMAIL>",
      "ph": "<SHA256_PHONE>",
      "fn": "<SHA256_FIRST_NAME>",
      "ln": "<SHA256_LAST_NAME>",
      "ge": "<SHA256_GENDER>",
      "ct": "<SHA256_CITY>",
      "st": "<SHA256_STATE>",
      "zp": "<SHA256_ZIP>",
      "country": "<SHA256_COUNTRY>",
      "client_ip_address": "1.2.3.4",
      "client_user_agent": "Mozilla/5.0...",
      "fbp": "fb.1.1234567890.987654321",
      "fbc": "fb.1.1234567890.IwAR1234567890",
      "external_id": "<SHA256_EXTERNAL_ID>"
    },
    "custom_data": {
      "value": 99.99,
      "currency": "BRL",
      "content_name": "Produto XYZ",
      "content_type": "product",
      "content_ids": ["SKU123"],
      "transaction_id": "order-12345",
      "content_category": "Eletronicos"
    }
  }]
}
```

### 4.3 Parametros user_data (Hashing SHA-256)

| Parametro | Hashing | Descricao |
|-----------|---------|-----------|
| em | SHA256 | Email (lowercase, trim) |
| ph | SHA256 | Telefone (+5511999999999) |
| fn | SHA256 | Primeiro nome |
| ln | SHA256 | Sobrenome |
| ge | SHA256 | Genero (m/f) |
| ct | SHA256 | Cidade |
| st | SHA256 | Estado (2 letras) |
| zp | SHA256 | CEP |
| country | SHA256 | Pais (2 letras) |
| client_ip_address | NAO hash | IP do cliente |
| client_user_agent | NAO hash | User-Agent |
| fbp | NAO hash | Facebook Browser ID cookie |
| fbc | NAO hash | Facebook Click ID cookie |
| external_id | SHA256 | ID externo do usuario |

### 4.4 action_source Values

| Valor | Descricao |
|-------|-----------|
| website | Evento de website |
| app | Evento de aplicativo |
| physical_store | Loja fisica (ate 62 dias retroativos) |
| phone_call | Chamada telefonica |
| chat | Chat/mensagem |
| email | Email marketing |
| business_messaging | WhatsApp/Messenger Business |

### 4.5 Deduplicacao Pixel + CAPI

Para evitar contagem dupla, envie o **mesmo `event_id`** tanto no Pixel quanto no CAPI:

```javascript
// PIXEL (browser)
fbq('track', 'Purchase', {value: 99.99, currency: 'BRL'}, {eventID: 'nonce_abc123'});

// CAPI (server) — mesmo event_id
{
  "event_name": "Purchase",
  "event_id": "nonce_abc123",
  ...
}
```

**Regras de deduplicacao:**
- Match por: `event_name` + `event_id` + `fbp`/`fbc` + `external_id`
- Janela de deduplicacao: **48 horas**
- Ambos (Pixel e CAPI) devem enviar o mesmo `event_id`

### 4.6 Limites e Boas Praticas

- **Max 1,000 eventos** por request batch
- **event_time** aceita timestamps ate **7 dias** antes do envio (62 dias para `physical_store`)
- Envie eventos **imediatamente** apos ocorrencia (preferencialmente em ate 1 hora)
- Se qualquer evento no batch for invalido, o **batch inteiro e rejeitado**
- Eventos visiveis no Events Manager em ate **20 minutos**
- **Business SDKs** fazem hashing automaticamente (PHP >=7.2, Node.js >=7.6, Java >=8, Python >=2.7, Ruby >=2)

### 4.7 Test Events

```json
{
  "data": [{ "event_name": "Purchase", "event_time": 1764975551, ... }],
  "test_event_code": "TEST12345"
}
```

Gere o `test_event_code` em: **Events Manager > Data Sources > Pixel > Test Events**

**IMPORTANTE:** Remova `test_event_code` antes de ir para producao.

### 4.8 Event Match Quality (EMQ)

Score de 1-10 baseado na completude dos dados do usuario:

| Dados enviados | Score aprox. |
|----------------|-------------|
| IP + UA + fbp/fbc apenas | ~4/10 |
| + email | ~6/10 |
| + email + phone + name | ~8/10 |
| Dados completos | ~10/10 |

### 4.9 Conversions API Gateway (CAPIG)

Alternativa que converte automaticamente eventos do Pixel web em eventos server-side:
- Preco: $10-100/mes
- Inclui Event Enhancement (cookie `gtmeec` para dados persistentes)
- Sem necessidade de desenvolvimento server-side

### 4.10 Compliance (LGPD/CCPA)

```json
{
  "data_processing_options": ["LDU"],
  "data_processing_options_country": 1,
  "data_processing_options_state": 1000
}
```

`state` codes: 1000 = California, 0 = geolocalizacao automatica

---

## 5. Autenticacao & Access Tokens

### 5.1 Tipos de Token

| Tipo | Duracao | Uso |
|------|---------|-----|
| User Token | ~1 hora | Testes, acesso temporario |
| Long-lived User Token | ~60 dias | Aplicacoes web |
| System User Token | Nao expira | Automacao server-to-server |
| Page Token | Varia | Operacoes de pagina |

### 5.2 Fluxo OAuth 2.0

```
https://www.facebook.com/v25.0/dialog/oauth?
  client_id={APP_ID}&
  redirect_uri={REDIRECT_URI}&
  scope=ads_management,ads_read
```

### 5.3 Permissoes Necessarias

| Permissao | Escopo |
|-----------|--------|
| ads_read | Leitura de campanhas e insights |
| ads_management | CRUD completo em campanhas |
| business_management | Administracao do Business Manager |

### 5.4 Access Tiers

| Tier | Aprovacao | Limites |
|------|-----------|---------|
| Standard | Automatica | Volumes limitados, 1 system user |
| Advanced | App Review | Volumes maiores, ate 10 system users |

**Manutencao Advanced Access:** Minimo 1,500 chamadas bem-sucedidas em janela de 15 dias, taxa de erro <15%.

---

## 6. Rate Limiting

### 6.1 Business Use Case (BUC) Scoring

| Operacao | Pontos |
|----------|--------|
| Read (GET) | 1 ponto |
| Write (POST/DELETE) | 3 pontos |

| Tier | Max pontos | Decay | Lockout |
|------|-----------|-------|---------|
| Development | 60 | 300s | 300s |
| Standard | 9,000 | 300s | 60s |

### 6.2 Limites por Ad Account (por hora)

| Operacao | Development | Standard |
|----------|-------------|----------|
| ads_management | 50K + 40*active_ads | 100K + 40*active_ads |
| custom_audience | 95K + 40*active_audiences | 190K + 40*active_audiences |
| ads_insights | 95K + 400*active_ads | 190K + 400*active_ads |

### 6.3 Limites Especiais

- **Mutacoes:** Max 100 requests/segundo por ad account/app
- **Budget changes:** Max 4 alteracoes/hora por ad set (lockout de 1 hora se exceder)
- **Account spending limit:** Max 10 alteracoes/dia

### 6.4 Headers de Resposta

```
X-Ad-Account-Usage:
  acc_id_util_pct: 45.2          # % de utilizacao
  ads_api_access_tier: standard   # Tier atual
  reset_time_duration: 180        # Segundos para reset

X-Business-Use-Case:
  call_count: 2500                # Chamadas no periodo
  total_cputime: 120              # CPU consumido (backend)
  estimated_time_to_regain_access: 0  # Countdown para recuperacao
```

### 6.5 Boas Praticas

1. Implementar **exponential backoff** para throttling
2. **Batch requests** para reduzir contagem de chamadas
3. Usar **async requests** para Insights (grandes volumes)
4. Monitorar **X-Business-Use-Case** headers proativamente
5. Cachear dados que nao mudam frequentemente

---

## 7. Error Codes

### 7.1 Codigos Principais

| Code | Subcode | Descricao | Acao |
|------|---------|-----------|------|
| 1 | — | Erro desconhecido | Retry com backoff |
| 2 | — | Servico temporariamente indisponivel | Retry apos 5 min |
| 4 | — | Insights throttle | Aguardar reset |
| 17 | — | User request limit | Aguardar reset |
| 100 | — | Parametro invalido | Verificar campo |
| 100 | 1487694 | Budget invalido | Verificar daily_budget |
| 190 | — | OAuth token invalido | Renovar token |
| 200 | — | Permissao negada | Verificar permissoes |
| 294 | — | Permissoes insuficientes | Solicitar permissao |
| 613 | — | Account throttle | Budget alterado >4x/hora |
| 80000-80014 | — | BUC rate limit excedido | Aguardar lockout |

### 7.2 Estrutura de Erro

```json
{
  "error": {
    "message": "Invalid parameter",
    "type": "OAuthException",
    "code": 100,
    "error_subcode": 1487694,
    "fbtrace_id": "ABC123",
    "blame_field_specs": [["daily_budget"]]
  }
}
```

`blame_field_specs` indica quais campos causaram o erro. Suporta campos nested: `["targeting_spec", "interested_in"]`.

---

## 8. API Versioning

- **Versao atual:** v25.0
- **Ciclo:** Novas versoes a cada ~3-4 meses
- **Deprecation:** Versoes antigas deprecadas ~2 anos apos lancamento
- **Mudanca proxima:** Legacy Advantage Shopping/App Campaign APIs deprecated ate Q1 2026

**Boas praticas:**
- Sempre especifique a versao na URL (`/v25.0/`)
- Monitore o changelog oficial para breaking changes
- Teste em sandbox antes de atualizar versao

---

## Fontes Oficiais

1. [Marketing API Overview](https://developers.facebook.com/docs/marketing-api)
2. [API Reference](https://developers.facebook.com/docs/marketing-api/reference/)
3. [Campaign Structure](https://developers.facebook.com/docs/marketing-api/campaign-structure/)
4. [Custom Audiences](https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences/)
5. [Lookalike Audiences](https://developers.facebook.com/docs/marketing-api/audiences/guides/lookalike-audiences/)
6. [Detailed Targeting](https://developers.facebook.com/docs/marketing-api/audiences/reference/detailed-targeting/)
7. [Insights API](https://developers.facebook.com/docs/marketing-api/insights/)
8. [Breakdowns](https://developers.facebook.com/docs/marketing-api/insights/breakdowns/)
9. [Reporting](https://developers.facebook.com/docs/marketing-api/reporting/)
10. [Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/)
11. [Using CAPI](https://developers.facebook.com/docs/marketing-api/conversions-api/using-the-api/)
12. [Rate Limiting](https://developers.facebook.com/docs/marketing-api/overview/rate-limiting/)
13. [Authorization](https://developers.facebook.com/docs/marketing-api/get-started/authorization/)
14. [Error Reference](https://developers.facebook.com/docs/marketing-api/error-reference/)
