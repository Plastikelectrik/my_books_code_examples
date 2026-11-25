export REA_BROWSER_OBSERVE_ENABLED=1
CDP='["http://127.0.0.1:9222"]'
ORIGINS='["http://127.0.0.1:8000"]'
export REA_BROWSER_CDP_ENDPOINTS_JSON="$CDP"
export REA_BROWSER_ALLOWED_ORIGINS_JSON="$ORIGINS"
rea list-browser-targets http://127.0.0.1:9222 --approved
