#!/usr/bin/env python3
"""Generate static Moni docs pages (one HTML file per language)."""

from pathlib import Path

from i18n_shared import LANG_PAGES, lang_grid_html, lang_menu_html, landing_lang_href

T = {
    "en": {
        "html_lang": "en",
        "page_title": "Moni — AI Ledger Companion for hledger",
        "meta_desc": "Moni is a local-first desktop companion for personal and small-business accounting with hledger.",
        "lang_menu_label": "Change language",
        "lang_menu_aria": "Language selector",
        "current_lang": "English",
        "brand": "Moni",
        "logo_alt": "Moni logo",
        "nav_manual": "Manual",
        "nav_feedback": "Feedback",
        "nav_features": "Features",
        "nav_video": "Video",
        "nav_screenshots": "Screenshots",
        "nav_languages": "Languages",
        "nav_download": "Download",
        "nav_license": "License",
        "nav_cta": "Get Moni",
        "hero_badge": "Local-first · AI-ready",
        "hero_title": "Modern Output,",
        "hero_gradient": "Neural Insights",
        "hero_suffix": "for your finances",
        "hero_subtitle": "A desktop companion for personal and small-business ledgers powered by hledger. Reports and registers on one side, optional AI chat on the other — your journal stays plain text on your machine.",
        "pta_label": "Foundation",
        "pta_title": "Plain text accounting & hledger",
        "pta_p1": "Plain text accounting (PTA) keeps your ledger as human-readable text files — dated transactions and account postings you can open in any editor, back up with git, and automate with scripts. No proprietary database locking you in.",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> is a fast, dependable command-line tool that reads those journal files and produces balances, registers, and reports. Moni wraps hledger in a modern desktop UI — same data, same power, easier to use every day.',
        "pta_p3": "Because everything is plain text and standard CLI commands, hledger integrates cleanly with the rest of your toolchain — grep, git, Python, spreadsheets, cron jobs, and AI scripts can read or transform your journal without a special export step. That power comes with a learning curve: flags, queries, and report syntax take time to memorize.",
        "pta_p4": "Moni keeps the same journal and hledger engine, but smooths daily work — one-click custom buttons for repeatable commands, built-in charts for visual summaries, and a fully functional hledger-web-style browse UI for accounts, registers, and reports. Use the GUI when you want speed; drop to the CLI anytime you still need raw power.",
        "journal_caption": "Example journal entry",
        "features_label": "Capabilities",
        "features_title": "CLI power. GUI clarity. Your data.",
        "features_desc": "Moni wraps hledger in a modern desktop app with customizable shortcuts, import tools, and an optional AI copilot — without locking your ledger in someone else's cloud.",
        "f1t": "hledger-powered", "f1d": "Balances, accounts, transactions, and reports driven by your configured hledger binary and journal files.",
        "f2t": "Local first", "f2d": "Ledgers live as files on your machine. Back up, diff, and version them with the same tools you use for code.",
        "f3t": "AI copilot", "f3d": "Ask questions, explain entries, and draft actions. Run local models with llama.cpp or Ollama for privacy — or, if you prefer, connect cloud AI such as OpenAI, Claude, or Gemini.",
        "f4t": "Privacy by default", "f4d": "No central SaaS ledger. Cloud AI only when you configure it with your own API keys.",
        "f5t": "Custom buttons", "f5d": "Quick-access toolbar shortcuts for your favorite hledger workflows — fully customizable via YAML recipes.",
        "f6t": "Import & export", "f6d": "CSV import tools and interactive features to review, add, or edit entries with a few clicks.",
        "f7t": "Reports & registers", "f7d": "Interactive registers, balance sheets, and charts — the full hledger toolkit in a friendly interface.",
        "f8t": "Read-only by default", "f8d": "Journal writes are opt-in and audited. Explore safely before you commit changes.",
        "f9t": "Multilingual UI", "f9d": "Full interface in seven languages. Help docs and chat can follow your locale.",
        "f10t": "Cross-platform", "f10d": "Runs natively on Linux, Windows, and macOS — same experience everywhere.",
        "video_label": "Watch",
        "video_title": "See Moni in action",
        "video_desc": "A walkthrough of ledger panels, AI chat, reports, and everyday workflows.",
        "video_placeholder": "YouTube video — coming soon",
        "video_hint": "Set data-youtube-id on #video-wrap when ready",
        "shots_label": "Screenshots",
        "shots_title": "Built for daily ledger work",
        "shots_desc": "Browse the main workspace, AI chat, reports, and settings.",
        "shot1": "Main workspace — ledger panel & toolbar",
        "shot2": "Ask Moni — AI chat with journal context",
        "shot3": "Reports — balances, charts & registers",
        "shot4": "Settings — hledger, AI, and appearance",
        "shot5": "Import — CSV and data tools",
        "placeholder": "Screenshot placeholder",
        "carousel_prev": "Previous screenshot",
        "carousel_next": "Next screenshot",
        "carousel_aria": "Screenshot navigation",
        "langs_label": "Languages",
        "langs_title": "Speaks your language",
        "langs_desc": "Moni ships with a fully localized interface in these languages:",
        "download_label": "Download",
        "download_title": "Get Moni",
        "download_desc": "Free to download. Available for all major desktop platforms.",
        "dl_linux": "Linux", "dl_linux_desc": "Portable build. AppImage and tarball coming soon.",
        "dl_win": "Windows", "dl_win_desc": "Installer with Start Menu shortcut. Coming soon.",
        "dl_mac": "macOS", "dl_mac_desc": "Drag-and-drop DMG installer. Coming soon.",
        "coming_soon": "Coming soon ↓",
        "license_label": "License",
        "license_title": "Copyright Notice",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. All rights reserved.',
        "license_donation": "[Donationware / honorware license terms will appear here.]",
        "license_placeholder": "Detailed license terms and conditions will be published here.",
        "thankyou_alt": "Thank you from Runable.app",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. All rights reserved.',
        "moni_alt": "Moni mascot",
    },
    "ko": {
        "html_lang": "ko",
        "page_title": "Moni — hledger용 AI 분개장(Journal) 동반자",
        "meta_desc": "Moni는 hledger 기반 개인 및 소규모 사업용 로컬 우선 데스크톱 분개장(Journal) 동반자입니다.",
        "lang_menu_label": "언어 변경",
        "lang_menu_aria": "언어 선택",
        "current_lang": "한국어",
        "brand": "Moni",
        "logo_alt": "Moni 로고",
        "nav_manual": "매뉴얼",
        "nav_feedback": "피드백",
        "nav_features": "기능",
        "nav_video": "동영상",
        "nav_screenshots": "스크린샷",
        "nav_languages": "언어",
        "nav_download": "다운로드",
        "nav_license": "라이선스",
        "nav_cta": "Moni 받기",
        "hero_badge": "로컬 우선 · AI 준비",
        "hero_title": "현대적인 GUI와 인공지능을 더해",
        "hero_gradient": "",
        "hero_suffix": "재정관리를 도와드립니다.",
        "hero_subtitle": "hledger로 개인 및 소규모 사업 분개장(Journal)을 다루는 데스크톱 동반자. 한쪽은 보고서와 레지스터, 다른 쪽은 선택적 AI 채팅 — 분개장(Journal)은 사용자의 컴퓨터에서 일반 텍스트로 유지됩니다.",
        "pta_label": "기반",
        "pta_title": "일반 텍스트 회계와 hledger",
        "pta_p1": "일반 텍스트 회계(PTA)는 분개장(Journal)을 사람이 읽을 수 있는 텍스트 파일로 유지합니다 — 날짜가 있는 거래와 계정 분개를 어떤 편집기에서든 열고, git으로 백업하고, 스크립트로 자동화할 수 있습니다. 독점 데이터베이스에 갇히지 않습니다.",
        "pta_p2": '<a href="https://hledger.org/">hledger</a>는 이러한 저널 파일을 읽어 잔액, 레지스터, 보고서를 만들어 주는 빠르고 신뢰할 수 있는 명령줄 도구입니다. Moni는 hledger를 현대적인 데스크톱 UI로 감쌉니다 — 같은 데이터, 같은 힘, 매일 더 쉽게.',
        "pta_p3": "모든 것이 일반 텍스트와 표준 CLI 명령이기 때문에 hledger는 grep, git, Python, 스프레드시트, cron, AI 스크립트 등 다른 도구와 깔끔하게 연동됩니다 — 별도 내보내기 없이 저널을 읽고 변환할 수 있습니다. 그만큼 배울 것도 있습니다. 플래그, 쿼리, 보고서 문법을 익히는 데 시간이 걸립니다.",
        "pta_p4": "Moni는 같은 저널과 hledger 엔진을 유지하면서 일상 작업을 편하게 합니다 — 반복 명령은 원클릭 맞춤 버튼으로, 시각적 요약은 내장 차트로, 계정·레지스터·보고서는 hledger-web과 같은 탐색 UI로. 빠르게 쓰고 싶을 때는 GUI, 원시 CLI가 필요할 때는 언제든 명령줄로.",
        "journal_caption": "저널 항목 예시",
        "features_label": "기능",
        "features_title": "CLI의 파워, GUI의 명확함, 당신의 데이터",
        "features_desc": "Moni는 hledger를 현대적인 데스크톱 앱으로 감싸며, 맞춤 단축키, 가져오기 도구, 사용자가 선택할 수 있는 AI 어시스턴트를 제공합니다 — 분개장(Journal)을 타인의 클라우드에 올려놓지 않습니다.",
        "f1t": "hledger 기반", "f1d": "설정한 hledger 바이너리와 저널 파일로 잔액, 계정, 거래, 보고서를 구동합니다.",
        "f2t": "로컬 우선", "f2d": "분개장(Journal)은 사용자의 컴퓨터에 파일로 존재합니다. 코드처럼 백업, 비교, 버전 관리가 가능합니다.",
        "f3t": "AI 코파일럿", "f3d": "질문하고, 분개를 설명하고, 작업을 작성하세요. llama.cpp나 Ollama로 로컬 모델을 실행해 프라이버시를 지킬 수 있고, 원하면 OpenAI, Claude, Gemini 같은 클라우드 AI도 연결할 수 있습니다.",
        "f4t": "기본값은 프라이버시", "f4d": "중앙 SaaS 분개장(Journal) 없음. 클라우드 AI는 내 API 키로 설정할 때만 사용합니다.",
        "f5t": "맞춤 버튼", "f5d": "즐겨 쓰는 hledger 워크플로를 위한 도구 모음 단축키 — YAML 레시피로 완전히 맞춤 설정.",
        "f6t": "가져오기 및 내보내기", "f6d": "CSV 가져오기와 몇 번의 클릭으로 분개를 검토·추가·편집하는 대화형 기능.",
        "f7t": "보고서 및 레지스터", "f7d": "대화형 레지스터, 대차대조표, 차트 — 친숙한 UI에서 hledger 전체 도구 모음.",
        "f8t": "기본값은 읽기 전용", "f8d": "저널 쓰기는 선택 사항이며 감사됩니다. 변경 전에 안전하게 탐색하세요.",
        "f9t": "다국어 UI", "f9d": "7개 언어로 완전 현지화된 UI. 도움말과 채팅도 로케일을 따릅니다.",
        "f10t": "크로스 플랫폼", "f10d": "Linux, Windows, macOS에서 네이티브 실행 — 어디서나 같은 경험.",
        "video_label": "시청",
        "video_title": "Moni 동작 보기",
        "video_desc": "분개장(Journal) 패널, AI 채팅, 보고서, 일상 워크플로 둘러보기.",
        "video_placeholder": "YouTube 동영상 — 곧 공개",
        "video_hint": "준비되면 #video-wrap에 data-youtube-id 설정",
        "shots_label": "스크린샷",
        "shots_title": "매일의 분개장(Journal) 작업을 위해",
        "shots_desc": "메인 작업 공간, AI 채팅, 보고서, 설정을 살펴보세요.",
        "shot1": "메인 작업 공간 — 분개장(Journal) 패널 및 도구 모음",
        "shot2": "Moni에게 물어보기 — 저널 컨텍스트가 있는 AI 채팅",
        "shot3": "보고서 — 잔액, 차트 및 레지스터",
        "shot4": "설정 — hledger, AI 및 모양",
        "shot5": "가져오기 — CSV 및 데이터 도구",
        "placeholder": "스크린샷 자리 표시",
        "carousel_prev": "이전 스크린샷",
        "carousel_next": "다음 스크린샷",
        "carousel_aria": "스크린샷 탐색",
        "langs_label": "언어",
        "langs_title": "당신의 언어로",
        "langs_desc": "Moni는 다음 언어로 완전 현지화된 UI를 제공합니다:",
        "download_label": "다운로드",
        "download_title": "Moni 받기",
        "download_desc": "무료 다운로드. 모든 주요 데스크톱 플랫폼에서 이용 가능.",
        "dl_linux": "Linux", "dl_linux_desc": "휴대용 빌드. AppImage 및 tarball 곧 제공.",
        "dl_win": "Windows", "dl_win_desc": "시작 메뉴 바로 가기가 있는 설치 프로그램. 곧 제공.",
        "dl_mac": "macOS", "dl_mac_desc": "드래그 앤 드롭 DMG 설치 프로그램. 곧 제공.",
        "coming_soon": "곧 제공 ↓",
        "license_label": "라이선스",
        "license_title": "저작권 고지",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. 모든 권리 보유.',
        "license_donation": "[Donationware / honorware 라이선스 조항이 여기에 표시됩니다.]",
        "license_placeholder": "자세한 라이선스 조건은 여기에 게시됩니다.",
        "thankyou_alt": "Runable.app의 감사 인사",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. All rights reserved.',
        "moni_alt": "Moni 마스코트",
    },
    "zh": {
        "html_lang": "zh",
        "page_title": "Moni — hledger 的 AI 账本助手",
        "meta_desc": "Moni 是基于 hledger 的本地优先桌面账本助手，面向个人和小型企业。",
        "lang_menu_label": "更改语言",
        "lang_menu_aria": "语言选择",
        "current_lang": "中文",
        "brand": "Moni",
        "logo_alt": "Moni 标志",
        "nav_manual": "手册",
        "nav_feedback": "反馈",
        "nav_features": "功能",
        "nav_video": "视频",
        "nav_screenshots": "截图",
        "nav_languages": "语言",
        "nav_download": "下载",
        "nav_license": "许可",
        "nav_cta": "获取 Moni",
        "hero_badge": "本地优先 · AI 就绪",
        "hero_title": "Modern Output，",
        "hero_gradient": "神经网络洞察",
        "hero_suffix": "为您的财务",
        "hero_subtitle": "面向个人和小型企业账本的 hledger 桌面伴侣。一侧是报表和分类账，另一侧是可选的 AI 聊天 — 您的日记账仍是机器上的纯文本。",
        "pta_label": "基础",
        "pta_title": "纯文本记账与 hledger",
        "pta_p1": "纯文本记账（PTA）将账本保存为人类可读的文本文件 — 带日期的交易和账户分录，可在任何编辑器中打开，用 git 备份，用脚本自动化。不会被专有数据库锁住。",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> 是读取这些日记账文件并生成余额、分类账和报表的快速可靠命令行工具。Moni 为 hledger 提供现代桌面界面 — 同样的数据，同样的能力，日常使用更轻松。',
        "pta_p3": "由于一切都是纯文本和标准 CLI 命令，hledger 能与其他工具顺畅集成 — grep、git、Python、电子表格、cron 和 AI 脚本都可以读取或转换您的日记账，无需专门导出。这种能力也带来学习曲线：标志、查询和报表语法需要时间掌握。",
        "pta_p4": "Moni 保留相同的日记账和 hledger 引擎，但让日常工作更顺畅 — 可重复命令用一键自定义按钮，可视化摘要用内置图表，账户、分类账和报表则用功能完整的 hledger-web 风格浏览界面。想快时用 GUI，需要原始能力时随时回到 CLI。",
        "journal_caption": "日记账示例",
        "features_label": "能力",
        "features_title": "CLI 之力。GUI 之清。您的数据。",
        "features_desc": "Moni 将 hledger 包装为现代桌面应用，提供可定制快捷方式、导入工具和可选 AI 副驾驶 — 不会把账本锁在别人的云端。",
        "f1t": "hledger 驱动", "f1d": "通过您配置的 hledger 可执行文件和日记账文件驱动余额、账户、交易和报表。",
        "f2t": "本地优先", "f2d": "账本以文件形式保存在您的机器上。像代码一样备份、对比和版本管理。",
        "f3t": "AI 副驾驶", "f3d": "提问、解释分录并起草操作。使用 llama.cpp 或 Ollama 运行本地模型以保护隐私 — 若您愿意，也可连接 OpenAI、Claude、Gemini 等云端 AI。",
        "f4t": "默认隐私", "f4d": "无中央 SaaS 账本。仅在使用您自己的 API 密钥配置时才使用云端 AI。",
        "f5t": "自定义按钮", "f5d": "为您喜爱的 hledger 工作流提供工具栏快捷方式 — 可通过 YAML 配方完全定制。",
        "f6t": "导入与导出", "f6d": "CSV 导入和交互功能，几次点击即可查看、添加或编辑分录。",
        "f7t": "报表与分类账", "f7d": "交互式分类账、资产负债表和图表 — 在友好界面中使用完整 hledger 工具包。",
        "f8t": "默认只读", "f8d": "日记账写入需选择启用并受审计。在提交更改前可安全探索。",
        "f9t": "多语言界面", "f9d": "七种语言的完整本地化界面。帮助和聊天可跟随您的区域设置。",
        "f10t": "跨平台", "f10d": "原生运行于 Linux、Windows 和 macOS — 处处相同体验。",
        "video_label": "观看",
        "video_title": "观看 Moni 演示",
        "video_desc": "ledger 面板、AI 聊天、报表和日常工作流程导览。",
        "video_placeholder": "YouTube 视频 — 即将推出",
        "video_hint": "准备好后设置 #video-wrap 的 data-youtube-id",
        "shots_label": "截图",
        "shots_title": "为日常账本工作而设计",
        "shots_desc": "浏览主工作区、AI 聊天、报表和设置。",
        "shot1": "主工作区 — 账本面板与工具栏",
        "shot2": "询问 Moni — 带日记账上下文的 AI 聊天",
        "shot3": "报表 — 余额、图表与分类账",
        "shot4": "设置 — hledger、AI 与外观",
        "shot5": "导入 — CSV 与数据工具",
        "placeholder": "截图占位符",
        "carousel_prev": "上一张截图",
        "carousel_next": "下一张截图",
        "carousel_aria": "截图导航",
        "langs_label": "语言",
        "langs_title": "说您的语言",
        "langs_desc": "Moni 提供以下语言的完整本地化界面：",
        "download_label": "下载",
        "download_title": "获取 Moni",
        "download_desc": "免费下载。适用于所有主要桌面平台。",
        "dl_linux": "Linux", "dl_linux_desc": "便携版构建。AppImage 和 tarball 即将推出。",
        "dl_win": "Windows", "dl_win_desc": "带「开始」菜单快捷方式的安装程序。即将推出。",
        "dl_mac": "macOS", "dl_mac_desc": "拖放式 DMG 安装程序。即将推出。",
        "coming_soon": "即将推出 ↓",
        "license_label": "许可",
        "license_title": "版权声明",
        "license_copyright": '版权所有 © 2026 <a href="https://runable.app">Runable.app</a>。保留所有权利。',
        "license_donation": "［Donationware / honorware 许可条款将在此显示。］",
        "license_placeholder": "详细许可条款将在此发布。",
        "thankyou_alt": "来自 Runable.app 的感谢",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. All rights reserved.',
        "moni_alt": "Moni 吉祥物",
    },
    "ja": {
        "html_lang": "ja",
        "page_title": "Moni — hledger 向け AI レジャーコンパニオン",
        "meta_desc": "Moni は hledger 向けのローカルファーストデスクトップ元帳コンパニオンです。",
        "lang_menu_label": "言語を変更",
        "lang_menu_aria": "言語選択",
        "current_lang": "日本語",
        "brand": "Moni",
        "logo_alt": "Moni ロゴ",
        "nav_manual": "マニュアル",
        "nav_feedback": "フィードバック",
        "nav_features": "機能",
        "nav_video": "動画",
        "nav_screenshots": "スクリーンショット",
        "nav_languages": "言語",
        "nav_download": "ダウンロード",
        "nav_license": "ライセンス",
        "nav_cta": "Moni を入手",
        "hero_badge": "ローカルファースト · AI 対応",
        "hero_title": "Modern Output,",
        "hero_gradient": "ニューラルインサイト",
        "hero_suffix": "あなたの財務のために",
        "hero_subtitle": "hledger を使った個人・小規模事業向け元帳のデスクトップコンパニオン。レポートとレジスタが片側、オプションの AI チャットがもう片側 — ジャーナルはお使いのマシン上のプレーンテキストのまま。",
        "pta_label": "基盤",
        "pta_title": "プレーンテキスト会計と hledger",
        "pta_p1": "プレーンテキスト会計（PTA）は、元帳を人間が読めるテキストファイルとして保持します — 日付付きの取引と勘定への仕訳を、どのエディタでも開き、git でバックアップし、スクリプトで自動化できます。独自データベースに閉じ込められません。",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> はそのジャーナルファイルを読み取り、残高・レジスタ・レポートを生成する高速で信頼性の高いコマンドラインツールです。Moni は hledger をモダンなデスクトップ UI で包みます — 同じデータ、同じ力、日常使いがより簡単に。',
        "pta_p3": "すべてがプレーンテキストと標準 CLI コマンドなので、hledger は grep、git、Python、スプレッドシート、cron、AI スクリプトなど他のツールときれいに連携します — 特別なエクスポートなしでジャーナルを読み書きできます。その分、学習曲線もあります。フラグ、クエリ、レポート構文を覚えるには時間がかかります。",
        "pta_p4": "Moni は同じジャーナルと hledger エンジンを保ちながら、日常作業をスムーズにします — 繰り返しコマンドはワンクリックのカスタムボタン、視覚的な概要は内蔵チャート、口座・レジスタ・レポートは hledger-web 風の完全なブラウズ UI で。速く使いたいときは GUI、生の CLI が必要なときはいつでもコマンドラインへ。",
        "journal_caption": "ジャーナル記載例",
        "features_label": "機能",
        "features_title": "CLI の力。GUI の明快さ。あなたのデータ。",
        "features_desc": "Moni は hledger をモダンなデスクトップアプリで包み、カスタムショートカット、インポートツール、オプションの AI コパイロットを提供 — 元帳を他人のクラウドに閉じ込めません。",
        "f1t": "hledger 対応", "f1d": "設定した hledger バイナリとジャーナルファイルで残高、アカウント、取引、レポートを駆動。",
        "f2t": "ローカルファースト", "f2d": "元帳はマシン上のファイルとして存在。コードと同様にバックアップ、差分、バージョン管理。",
        "f3t": "AI コパイロット", "f3d": "質問、仕訳の説明、アクションの下書きができます。llama.cpp や Ollama でローカルモデルを動かせばプライバシーを保てます — 希望すれば OpenAI、Claude、Gemini などのクラウド AI も接続できます。",
        "f4t": "デフォルトでプライバシー", "f4d": "中央 SaaS 元帳なし。クラウド AI はご自身の API キーで設定した場合のみ。",
        "f5t": "カスタムボタン", "f5d": "お気に入りの hledger ワークフロー向けツールバーショートカット — YAML レシピでカスタマイズ可能。",
        "f6t": "インポートとエクスポート", "f6d": "CSV インポートと、数クリックで仕訳を確認・追加・編集するインタラクティブ機能。",
        "f7t": "レポートとレジスタ", "f7d": "インタラクティブなレジスタ、貸借対照表、チャート — フレンドリーな UI で hledger 全機能。",
        "f8t": "デフォルトは読み取り専用", "f8d": "ジャーナルへの書き込みはオプトインで監査付き。変更前に安全に探索。",
        "f9t": "多言語 UI", "f9d": "7 言語の完全ローカライズ UI。ヘルプとチャットもロケールに対応。",
        "f10t": "クロスプラットフォーム", "f10d": "Linux、Windows、macOS でネイティブ動作 — どこでも同じ体験。",
        "video_label": "視聴",
        "video_title": "Moni の動作を見る",
        "video_desc": "レジャーパネル、AI チャット、レポート、日常ワークフローのウォークスルー。",
        "video_placeholder": "YouTube 動画 — 近日公開",
        "video_hint": "準備ができたら #video-wrap に data-youtube-id を設定",
        "shots_label": "スクリーンショット",
        "shots_title": "日々の元帳作業のために",
        "shots_desc": "メインワークスペース、AI チャット、レポート、設定をご覧ください。",
        "shot1": "メインワークスペース — レジャーパネルとツールバー",
        "shot2": "Moni に聞く — ジャーナルコンテキスト付き AI チャット",
        "shot3": "レポート — 残高、チャート、レジスタ",
        "shot4": "設定 — hledger、AI、外観",
        "shot5": "インポート — CSV とデータツール",
        "placeholder": "スクリーンショットプレースホルダー",
        "carousel_prev": "前のスクリーンショット",
        "carousel_next": "次のスクリーンショット",
        "carousel_aria": "スクリーンショットナビゲーション",
        "langs_label": "言語",
        "langs_title": "あなたの言語で",
        "langs_desc": "Moni は以下の言語で完全ローカライズされた UI を提供します：",
        "download_label": "ダウンロード",
        "download_title": "Moni を入手",
        "download_desc": "無料でダウンロード。主要なデスクトッププラットフォームすべてに対応。",
        "dl_linux": "Linux", "dl_linux_desc": "ポータブルビルド。AppImage と tarball は近日公開。",
        "dl_win": "Windows", "dl_win_desc": "スタートメニューショートカット付きインストーラ。近日公開。",
        "dl_mac": "macOS", "dl_mac_desc": "ドラッグ＆ドロップ DMG インストーラ。近日公開。",
        "coming_soon": "近日公開 ↓",
        "license_label": "ライセンス",
        "license_title": "著作権表示",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. 全著作権所有。',
        "license_donation": "［Donationware / honorware ライセンス条項はここに表示されます。］",
        "license_placeholder": "詳細なライセンス条項はここに掲載されます。",
        "thankyou_alt": "Runable.app からの感謝メッセージ",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. All rights reserved.',
        "moni_alt": "Moni マスコット",
    },
    "es": {
        "html_lang": "es",
        "page_title": "Moni — Compañero de ledger con IA para hledger",
        "meta_desc": "Moni es un compañero de escritorio local-first para contabilidad personal y de pequeños negocios con hledger.",
        "lang_menu_label": "Cambiar idioma",
        "lang_menu_aria": "Selector de idioma",
        "current_lang": "Español",
        "brand": "Moni",
        "logo_alt": "Logo de Moni",
        "nav_manual": "Manual",
        "nav_feedback": "Comentarios",
        "nav_features": "Funciones",
        "nav_video": "Vídeo",
        "nav_screenshots": "Capturas",
        "nav_languages": "Idiomas",
        "nav_download": "Descargar",
        "nav_license": "Licencia",
        "nav_cta": "Obtener Moni",
        "hero_badge": "Local primero · listo para IA",
        "hero_title": "Modern Output,",
        "hero_gradient": "Perspectivas neuronales",
        "hero_suffix": "para tus finanzas",
        "hero_subtitle": "Un compañero de escritorio para libros contables personales y de pequeños negocios con hledger. Informes y registros a un lado, chat de IA opcional al otro — tu diario sigue siendo texto plano en tu máquina.",
        "pta_label": "Base",
        "pta_title": "Contabilidad en texto plano y hledger",
        "pta_p1": "La contabilidad en texto plano (PTA) mantiene tu ledger como archivos de texto legibles — transacciones fechadas y asientos a cuentas que puedes abrir en cualquier editor, respaldar con git y automatizar con scripts. Sin quedar atrapado en una base de datos propietaria.",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> es una herramienta de línea de comandos rápida y fiable que lee esos archivos de diario y produce saldos, registros e informes. Moni envuelve hledger en una interfaz de escritorio moderna — mismos datos, mismo poder, más fácil cada día.',
        "pta_p3": "Como todo es texto plano y comandos CLI estándar, hledger se integra bien con el resto de tu cadena de herramientas — grep, git, Python, hojas de cálculo, cron y scripts de IA pueden leer o transformar tu diario sin un paso de exportación especial. Ese poder tiene curva de aprendizaje: flags, consultas y sintaxis de informes llevan tiempo.",
        "pta_p4": "Moni mantiene el mismo diario y motor hledger, pero facilita el trabajo diario — botones personalizados de un clic para comandos repetibles, gráficos integrados para resúmenes visuales y una interfaz de exploración al estilo hledger-web para cuentas, registros e informes. Usa la GUI cuando quieras rapidez; vuelve al CLI cuando necesites potencia bruta.",
        "journal_caption": "Ejemplo de asiento",
        "features_label": "Capacidades",
        "features_title": "Poder CLI. Claridad GUI. Tus datos.",
        "features_desc": "Moni envuelve hledger en una app de escritorio moderna con accesos directos personalizables, herramientas de importación y un copiloto de IA opcional — sin encerrar tu ledger en la nube de otro.",
        "f1t": "Impulsado por hledger", "f1d": "Saldos, cuentas, transacciones e informes con tu binario hledger y archivos de diario configurados.",
        "f2t": "Local primero", "f2d": "Los ledgers viven como archivos en tu máquina. Respalda, compara y versiona como con código.",
        "f3t": "Copiloto de IA", "f3d": "Pregunta, explica asientos y redacta acciones. Ejecuta modelos locales con llama.cpp u Ollama para privacidad — o, si prefieres, conecta IA en la nube como OpenAI, Claude o Gemini.",
        "f4t": "Privacidad por defecto", "f4d": "Sin ledger SaaS central. IA en la nube solo cuando la configures con tus propias claves API.",
        "f5t": "Botones personalizados", "f5d": "Accesos rápidos en la barra de herramientas para tus flujos hledger favoritos — personalizables con recetas YAML.",
        "f6t": "Importar y exportar", "f6d": "Importación CSV y funciones interactivas para revisar, añadir o editar asientos con pocos clics.",
        "f7t": "Informes y registros", "f7d": "Registros interactivos, balances y gráficos — el kit completo de hledger en una interfaz amigable.",
        "f8t": "Solo lectura por defecto", "f8d": "Las escrituras en el diario son opt-in y auditadas. Explora con seguridad antes de confirmar cambios.",
        "f9t": "Interfaz multilingüe", "f9d": "Interfaz completa en siete idiomas. La ayuda y el chat pueden seguir tu locale.",
        "f10t": "Multiplataforma", "f10d": "Funciona nativamente en Linux, Windows y macOS — la misma experiencia en todas partes.",
        "video_label": "Ver",
        "video_title": "Moni en acción",
        "video_desc": "Un recorrido por paneles de ledger, chat de IA, informes y flujos diarios.",
        "video_placeholder": "Vídeo de YouTube — próximamente",
        "video_hint": "Configura data-youtube-id en #video-wrap cuando esté listo",
        "shots_label": "Capturas",
        "shots_title": "Hecho para el trabajo diario con ledgers",
        "shots_desc": "Explora el espacio de trabajo principal, chat de IA, informes y ajustes.",
        "shot1": "Espacio principal — panel de ledger y barra de herramientas",
        "shot2": "Pregunta a Moni — chat de IA con contexto del diario",
        "shot3": "Informes — saldos, gráficos y registros",
        "shot4": "Ajustes — hledger, IA y apariencia",
        "shot5": "Importar — CSV y herramientas de datos",
        "placeholder": "Marcador de captura",
        "carousel_prev": "Captura anterior",
        "carousel_next": "Captura siguiente",
        "carousel_aria": "Navegación de capturas",
        "langs_label": "Idiomas",
        "langs_title": "Habla tu idioma",
        "langs_desc": "Moni incluye una interfaz completamente localizada en estos idiomas:",
        "download_label": "Descargar",
        "download_title": "Obtener Moni",
        "download_desc": "Descarga gratuita. Disponible para todas las plataformas de escritorio principales.",
        "dl_linux": "Linux", "dl_linux_desc": "Build portable. AppImage y tarball próximamente.",
        "dl_win": "Windows", "dl_win_desc": "Instalador con acceso directo en el menú Inicio. Próximamente.",
        "dl_mac": "macOS", "dl_mac_desc": "Instalador DMG arrastrar y soltar. Próximamente.",
        "coming_soon": "Próximamente ↓",
        "license_label": "Licencia",
        "license_title": "Aviso de copyright",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. Todos los derechos reservados.',
        "license_donation": "[Los términos de licencia donationware/honorware aparecerán aquí.]",
        "license_placeholder": "Los términos de licencia detallados se publicarán aquí.",
        "thankyou_alt": "Gracias de Runable.app",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. Todos los derechos reservados.',
        "moni_alt": "Mascota Moni",
    },
    "de": {
        "html_lang": "de",
        "page_title": "Moni — KI-Ledger-Begleiter für hledger",
        "meta_desc": "Moni ist ein lokaler Desktop-Begleiter für private und kleine Geschäfts-Buchhaltung mit hledger.",
        "lang_menu_label": "Sprache ändern",
        "lang_menu_aria": "Sprachauswahl",
        "current_lang": "Deutsch",
        "brand": "Moni",
        "logo_alt": "Moni-Logo",
        "nav_manual": "Handbuch",
        "nav_feedback": "Feedback",
        "nav_features": "Funktionen",
        "nav_video": "Video",
        "nav_screenshots": "Screenshots",
        "nav_languages": "Sprachen",
        "nav_download": "Download",
        "nav_license": "Lizenz",
        "nav_cta": "Moni holen",
        "hero_badge": "Lokal zuerst · KI-bereit",
        "hero_title": "Modern Output,",
        "hero_gradient": "Neuronale Einblicke",
        "hero_suffix": "für Ihre Finanzen",
        "hero_subtitle": "Ein Desktop-Begleiter für private und kleine Geschäfts-Ledger mit hledger. Berichte und Kontenregister auf der einen Seite, optionaler KI-Chat auf der anderen — Ihr Journal bleibt Klartext auf Ihrem Rechner.",
        "pta_label": "Grundlage",
        "pta_title": "Klartext-Buchhaltung & hledger",
        "pta_p1": "Plain-Text-Accounting (PTA) hält Ihr Ledger als lesbare Textdateien — datierte Buchungen und Kontenposten, die Sie in jedem Editor öffnen, mit Git sichern und per Skript automatisieren können. Keine proprietäre Datenbank, die Sie einsperrt.",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> ist ein schnelles, zuverlässiges Kommandozeilen-Tool, das diese Journaldateien liest und Salden, Kontenregister und Berichte erzeugt. Moni verpackt hledger in eine moderne Desktop-Oberfläche — gleiche Daten, gleiche Kraft, im Alltag leichter zu nutzen.',
        "pta_p3": "Weil alles Klartext und Standard-CLI-Befehle sind, lässt sich hledger sauber in Ihre Toolchain einbinden — grep, git, Python, Tabellen, Cron und KI-Skripte können Ihr Journal ohne Spezialexport lesen oder verarbeiten. Diese Stärke hat eine Lernkurve: Flags, Abfragen und Berichtssyntax brauchen Zeit.",
        "pta_p4": "Moni behält dasselbe Journal und dieselbe hledger-Engine, erleichtert aber die tägliche Arbeit — Ein-Klick-Buttons für wiederkehrende Befehle, eingebaute Diagramme für visuelle Übersichten und eine voll funktionsfähige hledger-web-ähnliche Browse-Oberfläche für Konten, Register und Berichte. GUI für Tempo, CLI jederzeit für volle Kontrolle.",
        "journal_caption": "Beispiel-Journalbuchung",
        "features_label": "Funktionen",
        "features_title": "CLI-Power. GUI-Klarheit. Ihre Daten.",
        "features_desc": "Moni verpackt hledger in eine moderne Desktop-App mit anpassbaren Shortcuts, Import-Tools und optionalem KI-Copilot — ohne Ihr Ledger in einer fremden Cloud zu sperren.",
        "f1t": "hledger-basiert", "f1d": "Salden, Konten, Buchungen und Berichte über Ihr konfiguriertes hledger-Binary und Journaldateien.",
        "f2t": "Lokal zuerst", "f2d": "Ledger leben als Dateien auf Ihrem Rechner. Sichern, vergleichen und versionieren wie bei Code.",
        "f3t": "KI-Copilot", "f3d": "Fragen stellen, Buchungen erklären und Aktionen entwerfen. Lokale Modelle mit llama.cpp oder Ollama für Datenschutz — oder bei Bedarf Cloud-KI wie OpenAI, Claude oder Gemini.",
        "f4t": "Datenschutz standardmäßig", "f4d": "Kein zentrales SaaS-Ledger. Cloud-KI nur mit Ihren eigenen API-Schlüsseln.",
        "f5t": "Eigene Buttons", "f5d": "Schnellzugriff-Werkzeugleiste für Ihre hledger-Workflows — anpassbar per YAML-Rezepte.",
        "f6t": "Import & Export", "f6d": "CSV-Import und interaktive Funktionen zum Prüfen, Hinzufügen oder Bearbeiten von Buchungen.",
        "f7t": "Berichte & Register", "f7d": "Interaktive Register, Bilanzen und Diagramme — das volle hledger-Toolkit in freundlicher Oberfläche.",
        "f8t": "Standardmäßig schreibgeschützt", "f8d": "Journal-Schreibvorgänge sind opt-in und protokolliert. Sicher erkunden vor Änderungen.",
        "f9t": "Mehrsprachige Oberfläche", "f9d": "Vollständige Oberfläche in sieben Sprachen. Hilfe und Chat folgen Ihrer Locale.",
        "f10t": "Plattformübergreifend", "f10d": "Läuft nativ unter Linux, Windows und macOS — überall dieselbe Erfahrung.",
        "video_label": "Ansehen",
        "video_title": "Moni in Aktion",
        "video_desc": "Ein Rundgang durch Ledger-Panel, KI-Chat, Berichte und Alltags-Workflows.",
        "video_placeholder": "YouTube-Video — demnächst",
        "video_hint": "data-youtube-id auf #video-wrap setzen, wenn bereit",
        "shots_label": "Screenshots",
        "shots_title": "Für tägliche Ledger-Arbeit",
        "shots_desc": "Hauptarbeitsbereich, KI-Chat, Berichte und Einstellungen.",
        "shot1": "Hauptarbeitsbereich — Ledger-Panel & Toolbar",
        "shot2": "Moni fragen — KI-Chat mit Journal-Kontext",
        "shot3": "Berichte — Salden, Diagramme & Register",
        "shot4": "Einstellungen — hledger, KI und Erscheinungsbild",
        "shot5": "Import — CSV und Datentools",
        "placeholder": "Screenshot-Platzhalter",
        "carousel_prev": "Vorheriger Screenshot",
        "carousel_next": "Nächster Screenshot",
        "carousel_aria": "Screenshot-Navigation",
        "langs_label": "Sprachen",
        "langs_title": "Spricht Ihre Sprache",
        "langs_desc": "Moni liefert eine vollständig lokalisierte Oberfläche in diesen Sprachen:",
        "download_label": "Download",
        "download_title": "Moni holen",
        "download_desc": "Kostenlos herunterladen. Für alle gängigen Desktop-Plattformen.",
        "dl_linux": "Linux", "dl_linux_desc": "Portable Build. AppImage und Tarball demnächst.",
        "dl_win": "Windows", "dl_win_desc": "Installer mit Startmenü-Verknüpfung. Demnächst.",
        "dl_mac": "macOS", "dl_mac_desc": "Drag-and-Drop-DMG-Installer. Demnächst.",
        "coming_soon": "Demnächst ↓",
        "license_label": "Lizenz",
        "license_title": "Urheberrechtshinweis",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. Alle Rechte vorbehalten.',
        "license_donation": "[Donationware-/Honorware-Lizenzbedingungen erscheinen hier.]",
        "license_placeholder": "Ausführliche Lizenzbedingungen werden hier veröffentlicht.",
        "thankyou_alt": "Danke von Runable.app",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. Alle Rechte vorbehalten.',
        "moni_alt": "Moni-Maskottchen",
    },
    "fr": {
        "html_lang": "fr",
        "page_title": "Moni — Compagnon de ledger IA pour hledger",
        "meta_desc": "Moni est un compagnon de bureau local-first pour la comptabilité personnelle et de petites entreprises avec hledger.",
        "lang_menu_label": "Changer de langue",
        "lang_menu_aria": "Sélecteur de langue",
        "current_lang": "Français",
        "brand": "Moni",
        "logo_alt": "Logo Moni",
        "nav_manual": "Manuel",
        "nav_feedback": "Commentaires",
        "nav_features": "Fonctions",
        "nav_video": "Vidéo",
        "nav_screenshots": "Captures",
        "nav_languages": "Langues",
        "nav_download": "Télécharger",
        "nav_license": "Licence",
        "nav_cta": "Obtenir Moni",
        "hero_badge": "Local d'abord · prêt pour l'IA",
        "hero_title": "Modern Output,",
        "hero_gradient": "Insights neuronaux",
        "hero_suffix": "pour vos finances",
        "hero_subtitle": "Un compagnon de bureau pour les journaux personnels et de petites entreprises avec hledger. Rapports et registres d'un côté, chat IA optionnel de l'autre — votre journal reste du texte brut sur votre machine.",
        "pta_label": "Fondation",
        "pta_title": "Comptabilité en texte brut & hledger",
        "pta_p1": "La comptabilité en texte brut (PTA) conserve votre journal sous forme de fichiers texte lisibles — des transactions datées et des écritures sur des comptes que vous ouvrez dans n'importe quel éditeur, sauvegardez avec git et automatisez par script. Pas de base de données propriétaire qui vous enferme.",
        "pta_p2": '<a href="https://hledger.org/">hledger</a> est un outil en ligne de commande rapide et fiable qui lit ces fichiers journal et produit soldes, registres et rapports. Moni enveloppe hledger dans une interface de bureau moderne — mêmes données, même puissance, plus simple au quotidien.',
        "pta_p3": "Comme tout est en texte brut et en commandes CLI standard, hledger s'intègre proprement au reste de votre chaîne d'outils — grep, git, Python, tableurs, cron et scripts IA peuvent lire ou transformer votre journal sans export spécial. Cette puissance a une courbe d'apprentissage : flags, requêtes et syntaxe de rapports prennent du temps.",
        "pta_p4": "Moni garde le même journal et le même moteur hledger, mais facilite le travail quotidien — boutons personnalisés en un clic pour les commandes répétitives, graphiques intégrés pour les résumés visuels, et une interface de navigation de type hledger-web pour comptes, registres et rapports. GUI pour la rapidité, CLI quand vous voulez la puissance brute.",
        "journal_caption": "Exemple d'écriture",
        "features_label": "Capacités",
        "features_title": "Puissance CLI. Clarté GUI. Vos données.",
        "features_desc": "Moni enveloppe hledger dans une app de bureau moderne avec raccourcis personnalisables, outils d'import et copilote IA optionnel — sans enfermer votre ledger dans le cloud d'autrui.",
        "f1t": "Propulsé par hledger", "f1d": "Soldes, comptes, transactions et rapports via votre binaire hledger et fichiers journal configurés.",
        "f2t": "Local d'abord", "f2d": "Les journaux vivent en fichiers sur votre machine. Sauvegardez, comparez et versionnez comme du code.",
        "f3t": "Copilote IA", "f3d": "Posez des questions, expliquez des écritures et rédigez des actions. Exécutez des modèles locaux avec llama.cpp ou Ollama pour la confidentialité — ou, si vous le souhaitez, connectez une IA cloud comme OpenAI, Claude ou Gemini.",
        "f4t": "Confidentialité par défaut", "f4d": "Pas de ledger SaaS central. IA cloud uniquement si vous la configurez avec vos propres clés API.",
        "f5t": "Boutons personnalisés", "f5d": "Raccourcis barre d'outils pour vos workflows hledger favoris — personnalisables via recettes YAML.",
        "f6t": "Import et export", "f6d": "Import CSV et fonctions interactives pour consulter, ajouter ou modifier des écritures en quelques clics.",
        "f7t": "Rapports et registres", "f7d": "Registres interactifs, bilans et graphiques — la boîte à outils hledger complète dans une interface conviviale.",
        "f8t": "Lecture seule par défaut", "f8d": "Les écritures journal sont opt-in et auditées. Explorez en toute sécurité avant de valider des changements.",
        "f9t": "Interface multilingue", "f9d": "Interface complète en sept langues. L'aide et le chat peuvent suivre votre locale.",
        "f10t": "Multiplateforme", "f10d": "Fonctionne nativement sur Linux, Windows et macOS — la même expérience partout.",
        "video_label": "Regarder",
        "video_title": "Moni en action",
        "video_desc": "Une visite des panneaux ledger, du chat IA, des rapports et des workflows quotidiens.",
        "video_placeholder": "Vidéo YouTube — bientôt disponible",
        "video_hint": "Définir data-youtube-id sur #video-wrap quand prêt",
        "shots_label": "Captures",
        "shots_title": "Conçu pour le travail ledger quotidien",
        "shots_desc": "Parcourez l'espace de travail principal, le chat IA, les rapports et les paramètres.",
        "shot1": "Espace principal — panneau ledger et barre d'outils",
        "shot2": "Demandez à Moni — chat IA avec contexte journal",
        "shot3": "Rapports — soldes, graphiques et registres",
        "shot4": "Paramètres — hledger, IA et apparence",
        "shot5": "Import — CSV et outils de données",
        "placeholder": "Espace réservé capture",
        "carousel_prev": "Capture précédente",
        "carousel_next": "Capture suivante",
        "carousel_aria": "Navigation des captures",
        "langs_label": "Langues",
        "langs_title": "Parle votre langue",
        "langs_desc": "Moni propose une interface entièrement localisée dans ces langues :",
        "download_label": "Télécharger",
        "download_title": "Obtenir Moni",
        "download_desc": "Téléchargement gratuit. Disponible sur toutes les principales plateformes de bureau.",
        "dl_linux": "Linux", "dl_linux_desc": "Build portable. AppImage et tarball bientôt.",
        "dl_win": "Windows", "dl_win_desc": "Installeur avec raccourci menu Démarrer. Bientôt.",
        "dl_mac": "macOS", "dl_mac_desc": "Installeur DMG glisser-déposer. Bientôt.",
        "coming_soon": "Bientôt ↓",
        "license_label": "Licence",
        "license_title": "Avis de copyright",
        "license_copyright": 'Copyright © 2026 <a href="https://runable.app">Runable.app</a>. Tous droits réservés.',
        "license_donation": "[Les conditions de licence donationware/honorware apparaîtront ici.]",
        "license_placeholder": "Les conditions de licence détaillées seront publiées ici.",
        "thankyou_alt": "Merci de Runable.app",
        "footer_rights": '© 2026 <a href="https://runable.app">Runable.app</a>. Tous droits réservés.',
        "moni_alt": "Mascotte Moni",
    },
}

FEATURES = [
    ("⚡", "f1t", "f1d"),
    ("🏠", "f2t", "f2d"),
    ("🧠", "f3t", "f3d"),
    ("🔒", "f4t", "f4d"),
    ("🎛", "f5t", "f5d"),
    ("📥", "f6t", "f6d"),
    ("📈", "f7t", "f7d"),
    ("🛡", "f8t", "f8d"),
    ("🌐", "f9t", "f9d"),
    ("💻", "f10t", "f10d"),
]

SHOTS = [
    ("🖥", "shot1"),
    ("💬", "shot2"),
    ("📊", "shot3"),
    ("⚙️", "shot4"),
    ("📥", "shot5"),
]


def render(lang_code: str, filename: str) -> str:
    t = T[lang_code]
    features_html = "\n".join(
        f"""      <div class="feature-card">
        <div class="icon">{icon}</div>
        <h3>{t[tk]}</h3>
        <p>{t[dk]}</p>
      </div>"""
        for icon, tk, dk in FEATURES
    )
    shots_html = "\n".join(
        f"""        <div class="carousel-slide{" active" if i == 0 else ""}">
          <div class="slide-placeholder">
            <span class="ph-icon">{icon}</span>
            <span>{t["placeholder"]}</span>
          </div>
          <p class="slide-caption">{t[sk]}</p>
        </div>"""
        for i, (icon, sk) in enumerate(SHOTS)
    )
    if t.get("hero_gradient"):
        hero_h1_html = f"""      <span>{t["hero_title"]}</span><br>
      <span class="gradient">{t["hero_gradient"]}</span><br>
      <span>{t["hero_suffix"]}</span>"""
    else:
        hero_h1_html = f"""      <span>{t["hero_title"]}</span><br>
      <span>{t["hero_suffix"]}</span>"""
    return f"""<!DOCTYPE html>
<html lang="{t["html_lang"]}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{t["page_title"]}</title>
  <meta name="description" content="{t["meta_desc"]}">
  <link rel="icon" href="https://runableapp.github.io/i/favicon.ico" type="image/x-icon">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>
<body>

<nav>
  <div class="inner">
    <a href="#" class="brand">
      <img src="i/moni-wave.webp" alt="{t["logo_alt"]}">
      <span>{t["brand"]}</span>
    </a>
    <ul>
{lang_menu_html(
    menu_label=t["lang_menu_label"],
    menu_aria=t["lang_menu_aria"],
    links=[
        (landing_lang_href(code), flag, label, fname == filename)
        for code, fname, label, flag in LANG_PAGES
    ],
    current_flag=next(flag for code, fname, _label, flag in LANG_PAGES if fname == filename),
)}
      <li><a href="{"manual/index.html" if lang_code == "en" else f"manual/{lang_code}/index.html"}">{t["nav_manual"]}</a></li>
      <li><a href="feedback.html">{t["nav_feedback"]}</a></li>
      <li><a href="#download">{t["nav_download"]}</a></li>
      <li><a href="#license">{t["nav_license"]}</a></li>
      <li><a href="#download" class="nav-cta">{t["nav_cta"]}</a></li>
    </ul>
  </div>
</nav>

<section class="hero">
  <div class="hero-copy">
    <div class="hero-badge">
      <span class="dot" aria-hidden="true"></span>
      <span>{t["hero_badge"]}</span>
    </div>
    <h1>
{hero_h1_html}
    </h1>
    <p class="subtitle">{t["hero_subtitle"]}</p>
    <div class="hero-meta">
      <span>Linux</span>
      <span>Windows</span>
      <span>macOS</span>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-glow" aria-hidden="true"></div>
    <div class="hero-card">
      <img class="graph" src="i/graph.webp" alt="">
      <div class="moni-wrap">
        <img src="i/moni-standing.webp" alt="{t["moni_alt"]}">
      </div>
    </div>
  </div>
</section>

<section id="pta" class="pta-section alt">
  <div class="pta-grid">
    <div class="pta-copy">
      <p class="section-label">{t["pta_label"]}</p>
      <h2 class="section-title">{t["pta_title"]}</h2>
      <p>{t["pta_p1"]}</p>
      <p>{t["pta_p2"]}</p>
      <p>{t["pta_p3"]}</p>
      <p>{t["pta_p4"]}</p>
    </div>
    <div class="journal-card">
      <div class="journal-card-header">{t["journal_caption"]}</div>
      <pre class="journal-snippet">2025-03-15 * Coffee shop
    expenses:food:coffee        $4.50
    assets:checking:cash       $-4.50</pre>
    </div>
  </div>
</section>

<section id="features">
  <div class="container">
    <p class="section-label">{t["features_label"]}</p>
    <h2 class="section-title">{t["features_title"]}</h2>
    <p class="section-desc">{t["features_desc"]}</p>
    <div class="features-grid">
{features_html}
    </div>
  </div>
</section>

<section id="video" class="alt">
  <div class="container">
    <p class="section-label">{t["video_label"]}</p>
    <h2 class="section-title">{t["video_title"]}</h2>
    <p class="section-desc">{t["video_desc"]}</p>
    <div class="video-wrap" id="video-wrap" data-youtube-id="">
      <div class="video-placeholder">
        <div class="play-ring" aria-hidden="true">▶</div>
        <p>{t["video_placeholder"]}</p>
        <p class="small" style="font-size:0.82rem; opacity:0.7;">{t["video_hint"]}</p>
      </div>
    </div>
  </div>
</section>

<section id="screenshots">
  <div class="container">
    <p class="section-label">{t["shots_label"]}</p>
    <h2 class="section-title">{t["shots_title"]}</h2>
    <p class="section-desc">{t["shots_desc"]}</p>
    <div class="carousel">
      <button type="button" class="carousel-btn prev" aria-label="{t["carousel_prev"]}">‹</button>
      <div class="carousel-frame">
{shots_html}
      </div>
      <button type="button" class="carousel-btn next" aria-label="{t["carousel_next"]}">›</button>
      <div class="carousel-dots" role="tablist" aria-label="{t["carousel_aria"]}"></div>
    </div>
  </div>
</section>

<section id="languages" class="alt">
  <div class="container">
    <p class="section-label">{t["langs_label"]}</p>
    <h2 class="section-title">{t["langs_title"]}</h2>
    <p class="section-desc">{t["langs_desc"]}</p>
    <div class="lang-grid">
{lang_grid_html()}
    </div>
  </div>
</section>

<section id="download">
  <div class="container">
    <p class="section-label">{t["download_label"]}</p>
    <h2 class="section-title">{t["download_title"]}</h2>
    <p class="section-desc">{t["download_desc"]}</p>
    <div class="download-grid">
      <div class="download-card coming-soon">
        <div class="dl-icon" aria-hidden="true"><img src="i/os-linux.png" alt="Linux"></div>
        <h3>{t["dl_linux"]}</h3>
        <p>{t["dl_linux_desc"]}</p>
        <span class="format">{t["coming_soon"]}</span>
      </div>
      <div class="download-card coming-soon">
        <div class="dl-icon" aria-hidden="true"><img src="i/os-windows.png" alt="Windows"></div>
        <h3>{t["dl_win"]}</h3>
        <p>{t["dl_win_desc"]}</p>
        <span class="format">{t["coming_soon"]}</span>
      </div>
      <div class="download-card coming-soon">
        <div class="dl-icon" aria-hidden="true"><img src="i/os-apple.png" alt="macOS"></div>
        <h3>{t["dl_mac"]}</h3>
        <p>{t["dl_mac_desc"]}</p>
        <span class="format">{t["coming_soon"]}</span>
      </div>
    </div>
  </div>
</section>

<section id="license" class="alt">
  <div class="container">
    <p class="section-label">{t["license_label"]}</p>
    <h2 class="section-title">{t["license_title"]}</h2>
    <div class="license-box">
      <p>{t["license_copyright"]}</p>
      <p>{t["license_donation"]}</p>
      <p>{t["license_placeholder"]}</p>
    </div>
    <div class="thankyou-wrap">
      <img src="i/runable-thankyou-midsize.webp" alt="{t["thankyou_alt"]}">
    </div>
  </div>
</section>

<footer>
  <p>{t["footer_rights"]}</p>
</footer>

<script src="js/main.js"></script>
<script>
  (function () {{
    var wrap = document.getElementById("video-wrap");
    if (!wrap) return;
    var id = (wrap.getAttribute("data-youtube-id") || "").trim();
    if (!id) return;
    wrap.classList.add("has-video");
    var iframe = document.createElement("iframe");
    iframe.src = "https://www.youtube-nocookie.com/embed/" + encodeURIComponent(id) + "?rel=0";
    iframe.title = "Moni demo video";
    iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
    iframe.allowFullscreen = true;
    wrap.appendChild(iframe);
  }})();
</script>
</body>
</html>
"""


def main() -> None:
    out = Path(__file__).resolve().parent
    for lang_code, filename, _label, _flag in LANG_PAGES:
        path = out / filename
        path.write_text(render(lang_code, filename), encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
