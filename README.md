# an-info — LLM-вики о компании Anthropic

На ветке `main` сейчас находятся только файл лицензии [`LICENSE`](LICENSE) и корневой `README.md`. Основное содержимое проекта размещено в невлитой ветке [`claude/anthropic-public-benefit-fund-urtjcw`](https://github.com/svend4/an-info/tree/claude/anthropic-public-benefit-fund-urtjcw).

В той ветке реализована русскоязычная база знаний о компании Anthropic, организованная по паттерну «LLM wiki» Андрея Карпаты (октябрь 2026). Первая проработанная тема — **Anthropic Public Benefit Fund** (390 зафиксированных фактов `F001`–`F390` на 24 октября 2026 года).

## Структура проекта (по ветке `claude/anthropic-public-benefit-fund-urtjcw`)

```text
.
├── CLAUDE.md                                   # Схема вики: слои, правила ID, легенда статусов, операции
├── LICENSE                                     # Лицензия GNU AGPL v3.0
├── README.md                                   # Обзор вики и легенда статусов
├── raw/                                        # Неизменяемый слой сырых фактов на английском (4 файла)
│   ├── 2026-10-24_public-benefit-fund_facts.json  # Факты F001–F320 в JSON
│   ├── 2026-10-24_public-benefit-fund_facts.md    # Факты F001–F320 в Markdown
│   ├── 2026-10-24_methods_facts.json              # Факты F321–F390 в JSON
│   └── 2026-10-24_methods_facts.md                # Факты F321–F390 в Markdown
├── tools/
│   └── lint_wiki.py                            # Автоматический валидатор целостности вики
└── wiki/                                       # Русскоязычные страницы вики (12 Markdown-файлов)
    ├── index.md                                # Оглавление и сводные счётчики статусов
    ├── log.md                                  # Журнал загрузок и проверок
    ├── glossary.md                             # Глоссарий терминов с английскими оригиналами
    ├── anthropic-public-benefit-fund.md        # Главная статья-синтез (цитирует 157 фактов)
    ├── announcement-text.md                    # Разбор объявления от 18.10.2026 (F001–F025)
    ├── fund-mechanism.md                       # Механизм фонда и форма LLC vs 501(c)(3) (F226–F274)
    ├── finance-and-ipo.md                      # Оценка Anthropic, IPO и стоимость доли (F026–F070)
    ├── comparisons.md                          # Сравнение с OpenAI Foundation, CZI и др. (F071–F122)
    ├── reactions.md                            # Реакции и критика по первоисточникам (F123–F167)
    ├── anthropic-context.md                    # Корпоративный контекст, LTBT, отчётность (F168–F225)
    ├── media-coverage.md                       # Освещение в русско- и иноязычных СМИ (F275–F320)
    └── methods.md                              # Подходы к распределению и экономические меры (F321–F390)
```

### Система проверки фактов (согласно `CLAUDE.md` и `wiki/index.md`)

- Каждый факт в `raw/` имеет неизменяемый идентификатор (`F001`–`F390`), источник, цитату и статус проверки:
  - `✅` проверено двумя независимыми проверками (23 факта на 24.10.2026);
  - `⚠️` спорно; `🔴` не подтверждено (1 факт — `F025`);
  - `🟢` первоисточник (164); `🟡` крупное СМИ (129); `🟠` вторичный источник (65); `⚪` оценка или мнение (8).
- Набор регламентированных операций в `CLAUDE.md`: `Ingest` (загрузка), `Query` (ответ со ссылками на ID), `Lint` (проверка целостности), `Verify` (двойная проверка статусов).

## Проверенный стек и команды (ветка `claude/anthropic-public-benefit-fund-urtjcw`)

- **Технологический стек**: Markdown + JSON-реестры фактов + Python 3 (только стандартная библиотека: `glob`, `json`, `os`, `re`, `sys`).
- **Проверка целостности вики** (проверяет наличие каждого ID из `raw/*_facts.json` на домашней странице, совпадение значков статуса и относительные `.md`-ссылки):

```bash
python3 -I tools/lint_wiki.py
```

## Ветки репозитория

- `main` — базовая ветка, содержит только [`LICENSE`](LICENSE) и корневой `README.md`.
- `claude/anthropic-public-benefit-fund-urtjcw` — основная рабочая ветка с полным корпусом (`CLAUDE.md`, `raw/`, `wiki/`, `tools/lint_wiki.py`); PR пока не открыт.
- `codex/readme-overview-20261118` — открытый черновик PR [#1](https://github.com/svend4/an-info/pull/1) с кратким описанием текущего состояния `main`.

## Лицензия

Проект распространяется под лицензией **GNU Affero General Public License v3.0 (AGPL-3.0)** — см. файл [`LICENSE`](LICENSE).
