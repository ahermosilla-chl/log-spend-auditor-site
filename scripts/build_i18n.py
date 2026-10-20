"""Render the landing page in English (/) and Spanish (/es/) from one template.

Usage: python3 scripts/build_i18n.py
Edit scripts/i18n/template.html for structure and the STRINGS below for copy.
Both languages must define exactly the same keys (checked at build time).
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "scripts/i18n/template.html").read_text(encoding="utf-8")

COMMUNITY = "https://logspendauditor.lemonsqueezy.com/checkout/buy/523549b0-405d-4bcf-a2f1-47c3e58e5934"
PRO = "https://logspendauditor.lemonsqueezy.com/checkout/buy/294c335c-f859-4297-9a2c-e9415ec3e669?checkout[discount_code]=LAUNCH69"
SUPPORT = "support@logspendauditor.com"
SHARED = {"community_url": COMMUNITY, "pro_url": PRO, "support_email": SUPPORT}

EN = {
    # meta / chrome
    "lang": "en", "og_locale": "en_US", "root": "", "canonical": "https://logspendauditor.com/",
    "title": "Log Spend Auditor — Find the Splunk ingest nobody uses",
    "description": "Find the Splunk data you pay to ingest but nobody searches. A read-only tool that runs on your own machine: free Quickscan, one-time Pro audit with evidence for every finding.",
    "og_description": "Find the Splunk data you pay to ingest but nobody searches — without sending your data anywhere.",
    "skip": "Skip to content", "brand_label": "Log Spend Auditor — home", "nav_label": "Primary",
    "nav_how": "How it works", "nav_report": "The report", "nav_pricing": "Pricing", "nav_security": "Security",
    "nav_cta": "Download Free",
    "other_lang": "es", "other_lang_href": "es/", "other_lang_short": "ES",
    "other_lang_label": "Ver esta página en español", "other_lang_name": "Español",
    "per_day": "day", "or": "or", "no": "No",
    # hero
    "hero_eyebrow": "For Splunk admins and platform teams",
    "hero_title": "Find where your Splunk ingest budget is going — without sending your data anywhere.",
    "hero_lead": "Splunk is priced by how much data you ingest, not by how much of it anyone uses. Log Spend Auditor compares your license usage with real searches, alerts and scheduled reports, and shows which data you are paying for that nobody looks at.",
    "cta_community": "Download Community — Free", "cta_pro": "Buy Pro — $69",
    "price_line": "Regular $99 · One-time purchase · License does not expire",
    "price_fine": "Launch price limited to the first 10 redemptions.",
    "chips_label": "Key properties",
    "chip_readonly": "Read-only", "chip_local": "Runs on your machine",
    "chip_nocreds": "No credentials needed (CSV mode)", "chip_notelemetry": "No telemetry",
    "result_tag": "synthetic demo data",
    "stat_ingest": "Observed ingest", "stat_datasets": "Datasets", "stat_analyzed": "analyzed", "stat_review": "To review",
    "result_sub": "Highest-impact candidates",
    "result_caption": "Quickscan output on the sample data bundled with the tool. Not customer data.",
    # problem
    "problem_eyebrow": "The problem",
    "problem_title": "Ingest keeps growing. Nobody can say what is safe to cut.",
    "problem_body": "Debug logging left on after an incident, a feed onboarded twice, sources for a project that ended last year. Each one adds to the bill, and without proof that nobody uses it, nobody wants to be the one who turns it off.",
    "problem_1_t": "You pay by volume", "problem_1_p": "Your Splunk cost follows the GB/day you ingest, whether anyone searches it or not.",
    "problem_2_t": "Usage is invisible", "problem_2_p": "License reports show what comes in. They don't show what anyone actually uses.",
    "problem_3_t": "Evidence settles it", "problem_3_p": "\"Zero searches, alerts or scheduled reports in 90 days\" is a conversation the data owner can say yes to.",
    # how it works
    "how_eyebrow": "How it works",
    "how_title": "Four steps, all on your own machine.",
    "how_body": "The tool reads aggregated metadata about volume and usage, never your raw events, and sends nothing to us.",
    "how_flow_label": "Log Spend Auditor processing steps",
    "s1_tag": "Input", "s1_title": "Your Splunk data", "s1_src_csv": "CSV exports", "s1_src_rest": "Read-only REST API",
    "s1_text": "License usage plus search, alert and scheduled-report activity.", "s1_note": "No raw events required.",
    "s2_tag": "Collect", "s2_title": "Read-only collector", "s2_p1": "Never changes Splunk", "s2_p2": "Runs locally", "s2_p3": "No telemetry",
    "s3_tag": "Analyze", "s3_title": "Analysis engine",
    "s3_p1": "Volume per index and sourcetype", "s3_p2": "Who searches it, and how often", "s3_p3": "Alerts and scheduled reports", "s3_p4": "Protects security and audit data",
    "s4_tag": "Result", "s4_pro_name": "Full audit",
    "s4_c1": "Total ingest and candidate volume", "s4_c2": "Top candidates", "s4_c3": "Terminal summary",
    "s4_p1": "Every dataset, classified", "s4_p2": "Evidence and explanation", "s4_p3": "Shareable HTML report",
    # report
    "report_eyebrow": "What you get",
    "report_title": "Every finding comes with its evidence.",
    "report_body": "The Pro report doesn't just list numbers. It explains in plain language why each dataset was flagged, so you can take it straight to the data owner.",
    "finding_label": "Example finding from the sample report",
    "finding_kicker": "Example from the sample report",
    "sig_ingest": "Ingest", "sig_searches": "Searches in 90 days", "sig_alerts": "Used by alerts", "sig_scheduled": "Scheduled reports",
    "finding_why": "This dataset appears as a candidate because it ingests 38.0 GB/day, has no interactive searches in the last 90 days, and was not found in alerts or scheduled saved searches.",
    "finding_rec_label": "Recommendation:", "finding_rec": "review the ingestion or filtering policy with the data owner.",
    "legend_title": "What each label means",
    "legend_waste": "High volume and no searches, alerts or scheduled reports in 90 days. The strongest candidates.",
    "legend_review": "Some signs of low use, but not enough to be sure. Worth a check with the owner.",
    "legend_value": "Used by alerts, scheduled reports or frequent searches. Keep it.",
    "legend_protected": "Security, audit and compliance data. Never flagged as waste, whatever the numbers say.",
    "legend_other": "Normal use, or not enough signal to classify. Shown so the inventory is complete.",
    "report_link": "Open the complete sample Pro report →",
    "report_link_short": "See a sample Pro report →",
    # pricing
    "pricing_eyebrow": "Pricing",
    "pricing_title": "Start free. Pay once if you need the full audit.",
    "pricing_body": "Community discovers the problem. Pro explains the problem.",
    "free": "Free", "no_license": "No license required",
    "community_tagline": "Find out whether there is a problem.",
    "c_f1": "Quickscan on your real environment", "c_f2": "Total observed ingest", "c_f3": "How much volume is worth reviewing", "c_f4": "Top candidates preview", "c_f5": "Full offline demo",
    "launch": "Launch", "price_launch": "$69", "launch_price": "launch price", "price_regular_short": "$99 regular",
    "pro_tagline": "Know exactly what to review, and why.",
    "one_time": "One-time purchase", "one_install": "1 active installation", "no_expire": "License does not expire",
    "p_f1": "Every dataset classified", "p_f2": "Evidence and explanation for each finding", "p_f3": "Data Value Score to prioritize", "p_f4": "Recommendations, risks and methodology", "p_f5": "HTML and Markdown report to share",
    "pro_fine": "Regular price $99 · One-time purchase. Launch price limited to the first 10 redemptions.",
    "upgrade_note": "Start with Community. Upgrade to Pro in the same application — no reinstall required.",
    "platforms_label": "Supported platforms", "available_now": "Available now", "coming_later": "Coming later",
    "plat_tested": "Built and tested on Ubuntu 22.04 LTS", "plat_glibc": "Requires glibc 2.35 or newer",
    "plat_wsl": "Today: use a Linux host or WSL2",
    # security
    "sec_eyebrow": "Security and privacy",
    "sec_title": "Your Splunk data stays in your environment.",
    "sec_body": "Built for teams that can't send operational data to a third party.",
    "sec_1_t": "Runs locally", "sec_1_p": "The analysis runs on your machine. There is no cloud service behind it.",
    "sec_2_t": "Read-only", "sec_2_p": "It never changes Splunk configuration or data.",
    "sec_3_t": "No telemetry", "sec_3_p": "The product collects no usage data or analytics.",
    "sec_4_t": "Credentials stay with you", "sec_4_p": "In CSV mode it needs none. In REST mode the token is read locally and never uploaded.",
    "sec_5_t": "Reports stay local", "sec_5_p": "Reports are generated and stored on your machine.",
    "sec_6_t": "Licensing only", "sec_6_p": "Pro contacts Lemon Squeezy only to activate and validate the license. No Splunk data is sent.",
    "sec_note": "The demo and the Community Quickscan make no network connections at all. Details in the <a href=\"privacy/\">Privacy</a> page.",
    # queries
    "q_eyebrow": "Free, no download",
    "q_title": "Three Splunk searches to see where your ingest goes.",
    "q_body": "Paste these into Splunk Search today. They need the <code>search</code> capability and read access to <code>_internal</code> and <code>_audit</code>. No admin role.",
    "q1_title": "1. Your biggest datasets, in GB/day", "q2_title": "2. Which indexes people actually search", "q3_title": "3. Sourcetypes that went quiet",
    "q_note": "Anything big in list 1 that never shows up in list 2 is worth a conversation. Matching them by hand gets slow past a few dozen datasets, and searches that reach data through macros, eventtypes, alerts or scheduled reports are easy to miss. That cross-check is what the free Quickscan automates.",
    # builder
    "builder_eyebrow": "Who builds this",
    "builder_title": "Built by an observability engineer, not a sales team.",
    "builder_p1": "I'm Alvaro, an engineer who designs and runs monitoring and observability platforms for enterprise clients. The same question comes up in every Splunk environment: which of this data are we still paying for, and does anyone use it? Answering it meant days of hand-written searches and spreadsheets.",
    "builder_p2": "Log Spend Auditor is that work turned into a tool: read-only, local, and explainable line by line. Questions or a problem with a run? Write to me directly at <a href=\"mailto:support@logspendauditor.com\">support@logspendauditor.com</a> and I will answer.",
    # faq
    "faq_title": "Questions Splunk admins ask first.",
    "faq_1_q": "Do I have to give the tool my Splunk credentials?",
    "faq_1_a": "No. In CSV mode you run the bundled searches yourself, export the results and point the tool at the folder. It never talks to Splunk. REST mode is optional and uses a read-only token you provide, which stays on your machine.",
    "faq_2_q": "What Splunk permissions does it need?",
    "faq_2_a": "The <code>search</code> capability plus read access to <code>_internal</code> (license usage) and <code>_audit</code> (search activity). No admin role. It never creates, modifies or deletes configuration or data.",
    "faq_3_q": "Why does the free download go through a checkout?",
    "faq_3_a": "Community is delivered through Lemon Squeezy so you get a permanent download link by email. It costs nothing and needs no license key.",
    "faq_4_q": "I'm on a Mac or Windows laptop. Can I use it?",
    "faq_4_a": "The current build runs on Linux x86_64 with glibc 2.35 or newer, for example a jump host, a VM or WSL2 with Ubuntu 22.04. Native macOS and Windows builds come later.",
    "faq_5_q": "Will it tell me to delete data?",
    "faq_5_a": "No. It classifies each index and sourcetype and shows the evidence behind it. Findings are candidates to review with the data owner; savings are an estimate, not a guarantee, and you decide what to change.",
    "faq_6_q": "What do I get with Pro that Quickscan doesn't show?",
    "faq_6_a": "The classification of every dataset, the evidence and explanation for each one, the Data Value Score, recommendations, risks and methodology, as an HTML and Markdown report you can share. <a href=\"sample-report/\">Here is a complete example.</a>",
    # final + footer
    "final_title": "See what your Splunk ingest is really used for.",
    "final_body": "Run the free Quickscan on your own machine in a few minutes. Your Splunk data stays there.",
    "trademark": "Splunk is a trademark of Splunk Inc. Log Spend Auditor is an independent product and is not affiliated with or endorsed by Splunk Inc.",
    "footer_label": "Footer", "privacy": "Privacy", "terms": "Terms", "support": "Support",
}

ES = {
    "lang": "es", "og_locale": "es_LA", "root": "../", "canonical": "https://logspendauditor.com/es/",
    "title": "Log Spend Auditor — Encuentra el ingest de Splunk que nadie usa",
    "description": "Encuentra los datos que pagas por ingerir en Splunk y que nadie consulta. Herramienta de solo lectura que corre en tu propio equipo: Quickscan gratis y auditoría Pro de pago único, con evidencia en cada hallazgo.",
    "og_description": "Encuentra los datos que pagas por ingerir en Splunk y que nadie consulta, sin enviar tus datos a ninguna parte.",
    "skip": "Saltar al contenido", "brand_label": "Log Spend Auditor — inicio", "nav_label": "Principal",
    "nav_how": "Cómo funciona", "nav_report": "El reporte", "nav_pricing": "Precios", "nav_security": "Seguridad",
    "nav_cta": "Descargar gratis",
    "other_lang": "en", "other_lang_href": "../", "other_lang_short": "EN",
    "other_lang_label": "View this page in English", "other_lang_name": "English",
    "per_day": "día", "or": "o", "no": "No",
    "hero_eyebrow": "Para administradores de Splunk y equipos de plataforma",
    "hero_title": "Descubre en qué se va tu presupuesto de ingest en Splunk, sin enviar tus datos a ninguna parte.",
    "hero_lead": "Splunk se cobra por la cantidad de datos que ingieres, no por cuánto de eso usa alguien. Log Spend Auditor cruza tu uso de licencia con las búsquedas, alertas y reportes programados reales, y te muestra qué datos estás pagando sin que nadie los mire.",
    "cta_community": "Descargar Community — Gratis", "cta_pro": "Comprar Pro — US$69",
    "price_line": "Precio normal US$99 · Pago único · La licencia no vence",
    "price_fine": "Precio de lanzamiento limitado a las primeras 10 compras.",
    "chips_label": "Características clave",
    "chip_readonly": "Solo lectura", "chip_local": "Corre en tu equipo",
    "chip_nocreds": "Sin credenciales (modo CSV)", "chip_notelemetry": "Sin telemetría",
    "result_tag": "datos de demo sintéticos",
    "stat_ingest": "Ingest observado", "stat_datasets": "Datasets", "stat_analyzed": "analizados", "stat_review": "Por revisar",
    "result_sub": "Candidatos de mayor impacto",
    "result_caption": "Resultado del Quickscan sobre los datos de ejemplo que trae la herramienta. No son datos de clientes.",
    "problem_eyebrow": "El problema",
    "problem_title": "El ingest no para de crecer. Nadie sabe qué se puede recortar.",
    "problem_body": "Logs de debug que quedaron activos después de un incidente, una fuente cargada dos veces, datos de un proyecto que terminó el año pasado. Cada uno suma a la factura y, sin pruebas de que nadie los usa, nadie quiere ser quien los apague.",
    "problem_1_t": "Pagas por volumen", "problem_1_p": "El costo de Splunk sigue los GB/día que ingieres, los consulte alguien o no.",
    "problem_2_t": "El uso no se ve", "problem_2_p": "Los reportes de licencia muestran lo que entra. No muestran lo que realmente se usa.",
    "problem_3_t": "La evidencia lo resuelve", "problem_3_p": "\"Cero búsquedas, alertas o reportes programados en 90 días\" es algo a lo que el dueño del dato puede decir que sí.",
    "how_eyebrow": "Cómo funciona",
    "how_title": "Cuatro pasos, todos en tu propio equipo.",
    "how_body": "La herramienta lee metadatos agregados de volumen y uso, nunca tus eventos crudos, y no nos envía nada.",
    "how_flow_label": "Pasos de procesamiento de Log Spend Auditor",
    "s1_tag": "Entrada", "s1_title": "Tus datos de Splunk", "s1_src_csv": "Exportaciones CSV", "s1_src_rest": "API REST de solo lectura",
    "s1_text": "Uso de licencia más actividad de búsquedas, alertas y reportes programados.", "s1_note": "No requiere eventos crudos.",
    "s2_tag": "Recolección", "s2_title": "Recolector de solo lectura", "s2_p1": "Nunca modifica Splunk", "s2_p2": "Corre localmente", "s2_p3": "Sin telemetría",
    "s3_tag": "Análisis", "s3_title": "Motor de análisis",
    "s3_p1": "Volumen por índice y sourcetype", "s3_p2": "Quién lo busca y con qué frecuencia", "s3_p3": "Alertas y reportes programados", "s3_p4": "Protege datos de seguridad y auditoría",
    "s4_tag": "Resultado", "s4_pro_name": "Auditoría completa",
    "s4_c1": "Ingest total y volumen candidato", "s4_c2": "Principales candidatos", "s4_c3": "Resumen en terminal",
    "s4_p1": "Cada dataset clasificado", "s4_p2": "Evidencia y explicación", "s4_p3": "Reporte HTML para compartir",
    "report_eyebrow": "Qué obtienes",
    "report_title": "Cada hallazgo viene con su evidencia.",
    "report_body": "El reporte Pro no es solo una lista de números. Explica en lenguaje simple por qué se marcó cada dataset, para que puedas llevarlo directo al dueño del dato.",
    "finding_label": "Hallazgo de ejemplo del reporte de muestra",
    "finding_kicker": "Ejemplo del reporte de muestra",
    "sig_ingest": "Ingest", "sig_searches": "Búsquedas en 90 días", "sig_alerts": "Usado en alertas", "sig_scheduled": "Reportes programados",
    "finding_why": "Este dataset aparece como candidato porque ingiere 38.0 GB/día, no tiene búsquedas interactivas en los últimos 90 días y no se encontró en alertas ni en búsquedas programadas.",
    "finding_rec_label": "Recomendación:", "finding_rec": "revisar la política de ingesta o filtrado con el dueño del dato.",
    "legend_title": "Qué significa cada etiqueta",
    "legend_waste": "Alto volumen y ninguna búsqueda, alerta ni reporte programado en 90 días. Los candidatos más claros.",
    "legend_review": "Hay señales de poco uso, pero no suficientes para estar seguros. Conviene revisarlo con el dueño.",
    "legend_value": "Lo usan alertas, reportes programados o búsquedas frecuentes. Se mantiene.",
    "legend_protected": "Datos de seguridad, auditoría y cumplimiento. Nunca se marcan como desperdicio, digan lo que digan los números.",
    "legend_other": "Uso normal, o sin señal suficiente para clasificar. Se muestran para que el inventario esté completo.",
    "report_link": "Abrir el reporte Pro de ejemplo completo (en inglés) →",
    "report_link_short": "Ver un reporte Pro de ejemplo →",
    "pricing_eyebrow": "Precios",
    "pricing_title": "Empieza gratis. Paga una sola vez si necesitas la auditoría completa.",
    "pricing_body": "Community descubre el problema. Pro lo explica.",
    "free": "Gratis", "no_license": "Sin licencia",
    "community_tagline": "Averigua si tienes un problema.",
    "c_f1": "Quickscan sobre tu entorno real", "c_f2": "Ingest total observado", "c_f3": "Cuánto volumen vale la pena revisar", "c_f4": "Vista previa de los principales candidatos", "c_f5": "Demo completa sin conexión",
    "launch": "Lanzamiento", "price_launch": "US$69", "launch_price": "precio de lanzamiento", "price_regular_short": "US$99 normal",
    "pro_tagline": "Sabe exactamente qué revisar y por qué.",
    "one_time": "Pago único", "one_install": "1 instalación activa", "no_expire": "La licencia no vence",
    "p_f1": "Cada dataset clasificado", "p_f2": "Evidencia y explicación de cada hallazgo", "p_f3": "Data Value Score para priorizar", "p_f4": "Recomendaciones, riesgos y metodología", "p_f5": "Reporte HTML y Markdown para compartir",
    "pro_fine": "Precio normal US$99 · Pago único. Precio de lanzamiento limitado a las primeras 10 compras.",
    "upgrade_note": "Empieza con Community. Pasa a Pro en la misma aplicación, sin reinstalar.",
    "platforms_label": "Plataformas soportadas", "available_now": "Disponible ahora", "coming_later": "Próximamente",
    "plat_tested": "Construido y probado en Ubuntu 22.04 LTS", "plat_glibc": "Requiere glibc 2.35 o superior",
    "plat_wsl": "Hoy: usa un host Linux o WSL2",
    "sec_eyebrow": "Seguridad y privacidad",
    "sec_title": "Tus datos de Splunk se quedan en tu entorno.",
    "sec_body": "Pensado para equipos que no pueden enviar datos operacionales a terceros.",
    "sec_1_t": "Corre localmente", "sec_1_p": "El análisis corre en tu equipo. No hay un servicio en la nube detrás.",
    "sec_2_t": "Solo lectura", "sec_2_p": "Nunca modifica la configuración ni los datos de Splunk.",
    "sec_3_t": "Sin telemetría", "sec_3_p": "El producto no recolecta datos de uso ni analítica.",
    "sec_4_t": "Las credenciales son tuyas", "sec_4_p": "En modo CSV no necesita ninguna. En modo REST el token se lee localmente y nunca se sube.",
    "sec_5_t": "Los reportes quedan en tu equipo", "sec_5_p": "Los reportes se generan y se guardan en tu máquina.",
    "sec_6_t": "Solo para la licencia", "sec_6_p": "Pro contacta a Lemon Squeezy solo para activar y validar la licencia. No se envían datos de Splunk.",
    "sec_note": "La demo y el Quickscan de Community no hacen ninguna conexión de red. Más detalles en la página de <a href=\"../privacy/\">Privacidad</a> (en inglés).",
    "q_eyebrow": "Gratis, sin descargar nada",
    "q_title": "Tres búsquedas de Splunk para ver en qué se va tu ingest.",
    "q_body": "Pégalas hoy en Splunk Search. Necesitan la capacidad <code>search</code> y acceso de lectura a <code>_internal</code> y <code>_audit</code>. No requieren rol de administrador.",
    "q1_title": "1. Tus datasets más grandes, en GB/día", "q2_title": "2. Qué índices busca realmente la gente", "q3_title": "3. Sourcetypes que dejaron de recibir datos",
    "q_note": "Todo lo grande de la lista 1 que nunca aparece en la lista 2 merece una conversación. Cruzarlas a mano se vuelve lento con más de unas pocas decenas de datasets, y es fácil pasar por alto los datos que se consultan a través de macros, eventtypes, alertas o reportes programados. Ese cruce es justamente lo que automatiza el Quickscan gratuito.",
    "builder_eyebrow": "Quién lo construye",
    "builder_title": "Hecho por un ingeniero de observabilidad, no por un equipo de ventas.",
    "builder_p1": "Soy Alvaro, ingeniero que diseña y opera plataformas de monitoreo y observabilidad para clientes empresariales. En cada entorno Splunk aparece la misma pregunta: ¿qué datos seguimos pagando y alguien los usa? Responderla significaba días de búsquedas escritas a mano y planillas.",
    "builder_p2": "Log Spend Auditor es ese trabajo convertido en herramienta: solo lectura, local y explicable línea por línea. ¿Dudas o algún problema al ejecutarla? Escríbeme directamente a <a href=\"mailto:support@logspendauditor.com\">support@logspendauditor.com</a> y te respondo.",
    "faq_title": "Lo primero que preguntan los administradores de Splunk.",
    "faq_1_q": "¿Tengo que darle mis credenciales de Splunk a la herramienta?",
    "faq_1_a": "No. En modo CSV tú ejecutas las búsquedas incluidas, exportas los resultados y le indicas la carpeta a la herramienta. Nunca se conecta a Splunk. El modo REST es opcional y usa un token de solo lectura que tú entregas y que no sale de tu equipo.",
    "faq_2_q": "¿Qué permisos de Splunk necesita?",
    "faq_2_a": "La capacidad <code>search</code> y acceso de lectura a <code>_internal</code> (uso de licencia) y <code>_audit</code> (actividad de búsquedas). No requiere rol de administrador. Nunca crea, modifica ni borra configuración o datos.",
    "faq_3_q": "¿Por qué la descarga gratuita pasa por un checkout?",
    "faq_3_a": "Community se entrega a través de Lemon Squeezy para que recibas por email un enlace de descarga permanente. No cuesta nada y no requiere clave de licencia.",
    "faq_4_q": "Uso un notebook Mac o Windows. ¿Puedo usarla?",
    "faq_4_a": "La versión actual corre en Linux x86_64 con glibc 2.35 o superior, por ejemplo un jump host, una VM o WSL2 con Ubuntu 22.04. Las versiones nativas para macOS y Windows vienen más adelante.",
    "faq_5_q": "¿Me va a decir que borre datos?",
    "faq_5_a": "No. Clasifica cada índice y sourcetype y muestra la evidencia detrás. Los hallazgos son candidatos para revisar con el dueño del dato; el ahorro es una estimación, no una garantía, y tú decides qué cambiar.",
    "faq_6_q": "¿Qué obtengo con Pro que el Quickscan no muestra?",
    "faq_6_a": "La clasificación de cada dataset, la evidencia y explicación de cada uno, el Data Value Score, recomendaciones, riesgos y metodología, en un reporte HTML y Markdown que puedes compartir. <a href=\"../sample-report/\">Aquí hay un ejemplo completo</a> (en inglés).",
    "final_title": "Descubre para qué se usa realmente tu ingest de Splunk.",
    "final_body": "Corre el Quickscan gratis en tu propio equipo en pocos minutos. Tus datos de Splunk se quedan ahí.",
    "trademark": "Splunk es una marca registrada de Splunk Inc. Log Spend Auditor es un producto independiente y no está afiliado ni respaldado por Splunk Inc.",
    "footer_label": "Pie de página", "privacy": "Privacidad (en inglés)", "terms": "Términos (en inglés)", "support": "Soporte",
}


from i18n_extra import EN_EXTRA, ES_EXTRA  # noqa: E402  (docs, validation and refund strings)

EN.update(EN_EXTRA)
ES.update(ES_EXTRA)
DOCS_TEMPLATE = (ROOT / "scripts/i18n/docs.html").read_text(encoding="utf-8")


def render(template: str, strings: dict, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(template.format_map({**strings, **SHARED}), encoding="utf-8")


if __name__ == "__main__":
    missing = set(EN) ^ set(ES)
    if missing:
        raise SystemExit(f"EN/ES keys differ: {sorted(missing)}")
    render(TEMPLATE, EN, ROOT / "index.html")
    render(TEMPLATE, ES, ROOT / "es/index.html")
    render(DOCS_TEMPLATE, EN, ROOT / "docs/index.html")
    render(DOCS_TEMPLATE, ES, ROOT / "es/docs/index.html")
    print("Rendered index.html, es/index.html, docs/index.html, es/docs/index.html")
