# HBO Max × Yuno · payment methods and processors by country (22 Oct 2026)

Deliverable: Google Sheet `11ooDgbANHoqxP2mK4loX2mMeMmerJMtU0SuszPGe5lc` ("HBO Max × Yuno · Payment methods and processors by country · gaps (Oct 2026)"), tabs Gaps / Full ranking / Summary by country.

- `apac.json`, `europe.json`, `latam.json`: market research per country (20 + 20 + 18 HBO Max markets, same list as the connections deck). For each country: the payment methods consumers use for digital subscriptions and the acquirers/PSPs a streaming merchant needs, each rated 1 to 10 for HBO Max (10 = must-have). Produced by three research agents on 22 Oct 2026 with ~45 web searches each; `source` is a URL when a search backed the item, else `knowledge` (analyst judgment).
- `yuno_coverage_full.json`: Yuno coverage per country from `tools/connections/lib.py` (y.uno/integrations directory 14 Oct 2026 + Payment Type list + code scan), all modes (not recurring-only).
- `match_gaps.py`: cross-check with alias table → `ranking.json` (962 items). Statuses: Live / Homologating / Integrated (code) / Elsewhere (connection exists in other markets, not listed for the country) / Partial / N/A / Generic / MISSING.
- `sheet_builder.py <sheetId>`: writes the three tabs and applies the house format (service account must be writer).

Caveats: ratings are judgment, not measured share. "Carrier and ISP billing" in Latin America reflects HBO Max's own telco distribution deals (help.hbomax.com partner pages), not a PSP connection Yuno could add; in APAC it is a real aggregator gap (Boku is live only in 6 countries). Local card schemes (Elo, Cartes Bancaires, eftpos, Troy...) are marked Partial because they ride on the card acquirers Yuno already has, not as separate methods.
