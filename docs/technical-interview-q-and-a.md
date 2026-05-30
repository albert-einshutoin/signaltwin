# SignalTwin Technical Interview Q&A

SignalTwin の技術理解を確認するための質問と模範回答です。難易度は 1 から 5 へ進むほど上がります。

## Level 1: Basic Product And Python Understanding

1. **Q: SignalTwin は何をするプロダクトですか。**  
   A: 既存の BMS 時系列データと WiFi CSI、PZT、音響、画像、熱画像、建物メタデータを組み合わせ、湿気、カビ、苔、通信劣化、構造・快適性リスクを推定する Building Health Forecast Engine です。

2. **Q: SignalTwin は BMS を置き換えますか。**  
   A: 置き換えません。BMS は現在状態の取得と設備制御を担い、SignalTwin はその上位で建物健康状態を解釈し、将来リスクや保守優先度を出します。

3. **Q: Minimal MVP で実行できる主な処理は何ですか。**  
   A: YAML シナリオの検証、ルールベースのリスク計算、JSON のリスクレポート、Markdown の保守レポート、RoomCI 互換 YAML の生成です。

4. **Q: Adapter-ready MVP の目的は何ですか。**  
   A: 実機なしで raw fixture を adapter に通し、schema-validated な normalized payload に変換して既存リスクエンジンまで流せることを確認することです。

5. **Q: このプロジェクトの CLI はどのライブラリで実装されていますか。**  
   A: Typer です。`python -m signaltwin.cli validate`、`run`、`demo`、`adapter inspect` などのコマンドを提供します。

6. **Q: スキーマ定義に Pydantic を使う利点は何ですか。**  
   A: 入力値の型、範囲、未知フィールドの扱いを実行時に検証でき、I/O 境界の契約をコードで表現できます。

7. **Q: `StrictBaseModel` の役割は何ですか。**  
   A: `extra="forbid"` により、スキーマに定義されていない入力フィールドを拒否する基底モデルです。

8. **Q: `FlexibleBaseModel` はどのような場合に使いますか。**  
   A: 追加フィールドを許可したい入力や将来拡張を受け入れたい境界で使います。ただし、現状の中心スキーマは主に strict です。

9. **Q: `RiskLevel` にはどの値が入りますか。**  
   A: `"low"`、`"medium"`、`"high"` の 3 種類です。

10. **Q: `Score` はどのような意味で使われていますか。**  
    A: リスクや drift などの数値スコアを表す `float` の別名です。多くのスコアは Pydantic の `Field(ge=0, le=1)` で 0 から 1 に制約されています。

11. **Q: `SignalTwinScenario` の主要な構成要素は何ですか。**  
    A: `scenario`、`building`、`asset`、`maintenance`、`bms`、`signals`、`expected` です。

12. **Q: `BmsContext` に含まれる代表的な項目を挙げてください。**  
    A: 7日平均温度、湿度、照度、音量、動作時間、流量イベント、HVAC 稼働時間、除湿稼働時間、平均電流、ON/OFF 変化数などです。

13. **Q: `Signals` にはどの信号グループがありますか。**  
    A: `wifi_csi`、`pzt`、`acoustic`、`thermal`、`visual` です。

14. **Q: `VisualDefect` は何を表しますか。**  
    A: 画像検査で検出された欠陥を表します。`type`、`severity`、任意の `area_ratio`、`length_m` を持ちます。

15. **Q: `RiskReport` には何が含まれますか。**  
    A: `asset_id`、`risk_scores`、`evidence`、`recommendation` が含まれます。

16. **Q: evidence が必要な理由は何ですか。**  
    A: リスクスコアの根拠を保守担当者やレビュー担当者が追えるようにするためです。説明可能性は MVP の重要な価値です。

17. **Q: CLI の `validate` コマンドは何を確認しますか。**  
    A: シナリオ YAML を読み込み、Pydantic スキーマに合うかを検証し、シナリオ名と asset ID を表示します。

18. **Q: CLI の `run` コマンドは何を生成しますか。**  
    A: `risk_report.json`、`maintenance_report.md`、`roomci_scenario.yml` を出力します。

19. **Q: CLI の `adapter inspect` はリスク計算をしますか。**  
    A: しません。設定された adapter を読み込み、normalized key、source name、payload fields を検証・表示するだけです。

20. **Q: No-hardware demo の意味は何ですか。**  
    A: 実センサー、サーバ、ダッシュボードを起動せず、fixture と既存コードだけでデモ成果物を再生成できる状態です。

## Level 2: Schema, CLI, And Data Flow

21. **Q: `normalize_scenario()` はなぜ必要ですか。**  
    A: nested な `SignalTwinScenario` から `building_id` や `asset_id` を明示した `NormalizedScenario` に変換し、リスクエンジンが扱いやすい形に揃えるためです。

22. **Q: `NormalizedScenario` と `SignalTwinScenario` の違いは何ですか。**  
    A: `SignalTwinScenario` は入力 YAML に近い構造で、`NormalizedScenario` は計算側で使いやすいように ID と主要オブジェクトを展開した内部表現です。

23. **Q: `calculate_risk_report()` は `SignalTwinScenario` と `NormalizedScenario` の両方を受け取れます。なぜですか。**  
    A: 呼び出し側の利便性を高めるためです。未正規化なら内部で `normalize_scenario()` を呼び、正規化済みならそのまま計算します。

24. **Q: `AdapterOutput` が `dataclass(frozen=True)` である理由は何が考えられますか。**  
    A: adapter の出力を不変の値オブジェクトとして扱い、後続処理で payload や source 情報が予期せず変わるのを防ぐためです。

25. **Q: `AdapterOutput.__post_init__()` は何をしていますか。**  
    A: `normalized_key` に対応する Pydantic モデルを選び、payload を検証したうえで `exclude_none=True` の dict に正規化しています。

26. **Q: `NormalizedKey` が `Literal` で定義されている利点は何ですか。**  
    A: `"bms"`、`"wifi_csi"` など許可された key だけを型として表せるため、adapter と payload model の対応関係を明確にできます。

27. **Q: adapter の責務と risk engine の責務を分ける理由は何ですか。**  
    A: 実機や capture program が変わっても adapter だけを差し替え、リスク計算ロジックを安定させるためです。

28. **Q: `AdapterError` に source と path が含まれる理由は何ですか。**  
    A: 複数 adapter や fixture を扱うとき、どの入力で失敗したかを運用・テストで特定しやすくするためです。

29. **Q: `docs/device-io-assumptions.md` はなぜ重要ですか。**  
    A: 実機前の fixture I/O と将来の capture program  assumptions を管理する source of truth だからです。

30. **Q: `fixtures/raw/*` の役割は何ですか。**  
    A: 実センサーや外部プログラムの出力を模した入力データです。adapter contract と no-hardware integration を検証するために使います。

31. **Q: `configs/adapter-fixtures.yml` を使う利点は何ですか。**  
    A: コードを変えずに fixture source や adapter 選択を切り替えられ、将来の device-specific adapter にも移行しやすくなります。

32. **Q: `risk_report.json` を Pydantic で再検証するテストの意味は何ですか。**  
    A: CLI が出力する JSON が内部スキーマと一致し、後続の API、dashboard、CI で安全に消費できることを確認できます。

33. **Q: `roomci_scenario.yml` を出力する理由は何ですか。**  
    A: SignalTwin のリスク推定結果を RoomCI などのスマートホーム・運用シナリオ検証に接続するためです。

34. **Q: `maintenance_report.md` はなぜ Markdown ですか。**  
    A: GitHub、CI artifact、レビュー、営業・保守向け共有で扱いやすく、人間が読める出力にするためです。

35. **Q: `expected: dict[str, Any]` の弱点は何ですか。**  
    A: 型安全性が低く、期待値の構造がコード上で保証されません。テストや将来の契約が複雑になるほど専用モデル化が望ましくなります。

36. **Q: `score` を 0 から 1 に制約する利点は何ですか。**  
    A: 複数リスクの比較、UI 表示、閾値判定、API 契約を統一しやすくなります。

37. **Q: `Field(default_factory=list)` を使う理由は何ですか。**  
    A: mutable default の共有を避け、インスタンスごとに新しい list を生成するためです。

38. **Q: `Field(default_factory=lambda: AssetMaterial())` は何を避けていますか。**  
    A: `AssetMaterial()` をクラス定義時に一度だけ作って共有する問題を避け、asset ごとに独立した default object を作ります。

39. **Q: `model_dump(exclude_none=True)` は adapter 出力で何を実現しますか。**  
    A: 未入力の optional field を落とし、後続処理が実際に存在する payload fields だけを見るようにします。

40. **Q: CLI エラーを `typer.Exit(code=1)` で返す意味は何ですか。**  
    A: CI や shell script が失敗を exit code で検知できるようにするためです。

## Level 3: Risk Engine And Testing

41. **Q: `maintenance_priority` はどのように決まりますか。**  
    A: moisture、mold、moss、wood deformation、crack/void、communication drift、comfort degradation の各リスクの最大値として計算されます。

42. **Q: `_clamp()` の役割は何ですか。**  
    A: 加算式で計算されたスコアを 0 から 1 に丸め、4 桁に round して出力の範囲を安定させます。

43. **Q: moisture risk の主な入力要因は何ですか。**  
    A: 湿度、露点マージン、cold spots、asset の moisture vulnerability、材料文脈、PZT attenuation、最終点検日数などです。

44. **Q: mold risk と moisture risk はどう違いますか。**  
    A: mold risk は湿度に加えて低照度、露点、mold vulnerability、清掃間隔などを重視します。moisture risk は水分・結露・材料劣化寄りです。

45. **Q: moss risk はどの入力に強く依存しますか。**  
    A: visual の `moss` defect、severity、area ratio、moss vulnerability、低照度、清掃間隔に依存します。

46. **Q: communication drift risk の代表的な信号は何ですか。**  
    A: CSI drift score、SNR delta、packet loss rate、retransmission rate、multipath change score、baseline similarity です。

47. **Q: comfort degradation risk はどの要素で上がりますか。**  
    A: HVAC 稼働時間、湿度、thermal gradient、unusual acoustic noise、平均電流、comfort degradation vulnerability などです。

48. **Q: `_recommendation()` は何を基準に保守アクションを選びますか。**  
    A: 最大リスク項目を選び、そのリスク種類に対応する maintenance type と action を返します。

49. **Q: `_priority()` の閾値を説明してください。**  
    A: 0.70 以上は high、0.60 以上は medium_high、0.40 以上は medium、0.25 以上は low_medium、それ未満は low です。

50. **Q: evidence が空の場合の fallback は何ですか。**  
    A: `"No high-impact risk evidence was detected."` が入ります。これにより `RiskReport.evidence` の `min_length=1` を満たせます。

51. **Q: `tests/test_mvp_regression.py` は何を守っていますか。**  
    A: 全シナリオが CLI から実行でき、JSON、Markdown、RoomCI YAML が生成され、出力が parse できることを守っています。

52. **Q: adapter-ready regression が守る最重要 contract は何ですか。**  
    A: raw fixture が全 normalized key に変換され、schema-valid payload として既存 risk engine に流せることです。

53. **Q: `adapter inspect` のテストで確認すべき観点は何ですか。**  
    A: 設定ファイルを読み、registry から adapter を解決し、各 source の出力 payload が schema validation を通り、失敗時に exit code 1 を返すことです。

54. **Q: `tests/test_raw_fixture_contracts.py` のようなテストが必要な理由は何ですか。**  
    A: fixture の形が adapter contract からズレたときに早く検出し、実機前の開発基盤が壊れるのを防ぐためです。

55. **Q: risk engine の単体テストで property-based testing を導入するなら何を確認しますか。**  
    A: どの入力でもスコアが 0..1 に収まること、optional field の欠落で例外にならないこと、閾値境界の priority が安定することを確認します。

56. **Q: threshold-based ルールのテストで重要な境界値は何ですか。**  
    A: 例えば湿度 70/75/80、露点マージン 1.5/2.5、CSI drift 0.15/0.25、priority 0.25/0.40/0.60/0.70 などです。

57. **Q: `pytest` の tmp_path を使う利点は何ですか。**  
    A: 出力ファイルをテストごとの一時ディレクトリに閉じ込め、既存 artifact を汚さず、並列実行にも強くできます。

58. **Q: CLI テストに `CliRunner` を使う理由は何ですか。**  
    A: shell を起動せず Python 内で Typer CLI を呼び出せるため、出力、exit code、生成物を簡単に検証できます。

59. **Q: JSON Schema や OpenAPI ではなく Pydantic テストだけでよい場面はどこですか。**  
    A: 現フェーズのように実サーバを持たず、Python 内部と artifact の shape を保証するだけなら Pydantic validation が軽量で十分です。

60. **Q: 今後 API サーバを実装したら追加すべきテストは何ですか。**  
    A: FastAPI の endpoint test、response model validation、error response、fixture/demo artifact の読み込み失敗、schema backward compatibility test です。

## Level 4: Adapter Architecture, Baseline, And Contracts

61. **Q: adapter replacement rule を説明してください。**  
    A: device や capture program は変わってよいが、adapter が返す normalized key と schema-valid payload は安定させ、risk engine を変更しないというルールです。

62. **Q: 新しい thermal camera adapter を追加するときの最小手順は何ですか。**  
    A: device I/O assumption を更新し、adapter class を実装し、registry/config に追加し、raw fixture と contract test を追加し、risk engine に触らず既存 pipeline を通します。

63. **Q: adapter が risk score を計算してはいけない理由は何ですか。**  
    A: source-specific な処理と product logic が混ざり、device 変更のたびにリスク計算が揺れるからです。adapter は正規化、risk engine は解釈に集中すべきです。

64. **Q: baseline store と risk scoring はなぜ分けるべきですか。**  
    A: baseline comparison は測定値の差分を示す機能であり、risk scoring は保守判断用の解釈です。混ぜると「実証済みリスク」と「開発用比較」の境界が曖昧になります。

65. **Q: fixture-based baseline は field evidence と言えますか。**  
    A: 言えません。実機前の baseline は product flow と contract を検証する開発 artifact であり、物理的な drift validation ではありません。

66. **Q: `real baseline collection` が始まる条件は何ですか。**  
    A: 選定された実機 hardware path と real adapter が schema-validated payload を安定して返せるようになった後です。

67. **Q: 最初の実機 path として BMS CSV + Thermal + Visual が推奨される理由は何ですか。**  
    A: 建物健康リスクの根拠を出しやすく、WiFi CSI、PZT、音響より信号処理リスクが低く、物理検証までの距離が短いからです。

68. **Q: WiFi CSI / PZT / Acoustic を後回しにする技術的理由は何ですか。**  
    A: calibration、環境依存、信号処理、再現性、baseline collection の難度が高く、初期の building-health evidence として不確実性が大きいためです。

69. **Q: `AdapterOutput.payload` を dict に戻している現在の設計上の弱点は何ですか。**  
    A: Pydantic で検証した後に型情報が薄まり、downstream で文字列 key lookup や `Any` が増えやすい点です。

70. **Q: その弱点を改善するならどう設計しますか。**  
    A: `AdapterOutput` を generic にし、`payload` を `BmsContext | WifiCsiSignal | ...` の型付き model として保持し、serialization edge でのみ `model_dump()` します。

71. **Q: `build_api_response()` が artifact を読み直す設計の利点は何ですか。**  
    A: no-hardware demo の実出力を API 契約に変換するため、artifact と future API shape の整合をテストしやすくなります。

72. **Q: `build_dashboard_view_model()` の役割は何ですか。**  
    A: API response から dashboard が使いやすい `risk_cards`、`evidence_items`、`adapter_sources`、`drift_groups`、`report_links` などの表示用構造に変換します。

73. **Q: dashboard contract が runtime dependency を持たない利点は何ですか。**  
    A: Streamlit、browser、database、hardware なしで shape をテストでき、UI 実装前に data contract を安定させられます。

74. **Q: `outputs/demo/api_response.example.json` を future UI が先に読むべき理由は何ですか。**  
    A: 実サーバ実装より前に UI が期待する data shape を固定し、API と dashboard の開発を疎結合にできるからです。

75. **Q: `drift_comparison` を API に含める意味は何ですか。**  
    A: risk score とは別に、baseline と current の数値差分を future dashboard で見せられるようにするためです。

76. **Q: strict schema が強すぎて問題になる場面はありますか。**  
    A: 外部 device output が未安定な初期探索では、strict schema が頻繁に壊れる可能性があります。その場合は raw capture 層と normalized contract 層を分けるべきです。

77. **Q: raw capture 層と normalized contract 層を分ける意味は何ですか。**  
    A: 実機固有のノイズや format 変更を raw layer に閉じ込め、SignalTwin の内部契約は normalized model として安定させるためです。

78. **Q: adapter registry の設計で気をつけることは何ですか。**  
    A: adapter 名の衝突、未知 adapter のエラー、import side effect、設定ファイルとの整合、テストで全登録 adapter を検証することです。

79. **Q: `source_family` と `normalized_key` はなぜ両方ありますか。**  
    A: family は人間向け・運用向けの分類、normalized key は内部 schema と risk engine が使う安定 key として役割を分けられます。

80. **Q: adapter config に path を持たせるときの注意点は何ですか。**  
    A: relative path の解決基準、存在確認、ディレクトリ traversal、CI 上の cwd 差異、エラー時の path 表示を明確にする必要があります。

## Level 5: Senior Design, Validation, And Product Engineering

81. **Q: SignalTwin の最大の technical moat はどこにありますか。**  
    A: センサー取得そのものではなく、BMS と非 BMS 信号を normalized contract に集約し、建物健康リスクと保守判断に変換する interpretation layer です。

82. **Q: 現在の MVP が「完成」と言える範囲と、言えない範囲を切り分けてください。**  
    A: no-hardware scenario、adapter-ready flow、fixture baseline、demo artifact、API/dashboard contract は完成範囲です。実機 capture、calibration、field baseline、physical drift validation、runtime service は未完成です。

83. **Q: 「実機なしでできている」と「実用できる」を混同しないために何を明示しますか。**  
    A: fixture は contract validation 用であり、現場での predictive accuracy や maintenance ROI はまだ検証していないと明示します。

84. **Q: 現場導入前に必要な validation plan を説明してください。**  
    A: まず BMS + Thermal + Visual の小規模現場で baseline を取り、点検結果と突合し、false positive/false negative を測定し、threshold と evidence 文言を調整します。

85. **Q: risk score の calibration をどう進めますか。**  
    A: 初期はルールベースで説明可能性を保ち、現場ラベルが集まったら閾値・重みを再推定し、最終的にモデル化する場合も evidence と monotonicity を維持します。

86. **Q: ML/anomaly detection を早期に入れすぎるリスクは何ですか。**  
    A: データ量とラベルが不足したまま精度を主張しやすく、説明可能性、再現性、顧客信頼を損ねる可能性があります。

87. **Q: PyOD を導入するならどの位置に置きますか。**  
    A: normalized feature vector から anomaly score を出す補助要素として置き、最終判断は risk engine の evidence と recommendation に統合します。

88. **Q: risk engine を rule-based から hybrid に移行するときの互換性戦略は何ですか。**  
    A: 既存 `RiskReport` schema を維持し、new model output を internal feature として追加し、golden scenario と field labeled cases で regression を守ります。

89. **Q: `dict[str, Any]` が増えると何が悪くなりますか。**  
    A: 型チェックが効かず、key typo、shape mismatch、serialization boundary の曖昧さが増え、レビューとリファクタリングのコストが上がります。

90. **Q: Python 3.14 以上を前提にしている場合、型設計で注意することは何ですか。**
    A: `list[str]` や `dict[str, Any]` は使えますが、より新しい構文に依存しすぎないこと、Pydantic v2 の挙動を前提にテストすることが必要です。

91. **Q: public API を作る前に artifact contract を固める利点は何ですか。**  
    A: API サーバの実装詳細に引きずられず、消費側が必要とするデータ構造を先に合意でき、サーバ追加時の変更範囲を減らせます。

92. **Q: FastAPI を導入する場合、既存コードのどこを handler から分離すべきですか。**  
    A: demo 実行、artifact 読み込み、API response build、validation は service 関数に残し、handler は request/response と error mapping に限定します。

93. **Q: Streamlit dashboard を作る場合、最初に直結すべきデータは何ですか。**  
    A: `outputs/demo/dashboard_view_model.example.json` です。まず static contract を表示し、後で API または live demo pipeline に差し替えます。

94. **Q: maintenance recommendation の説明責任を高めるには何を追加しますか。**  
    A: risk ごとの contribution breakdown、threshold hit list、入力欠損の表示、前回 baseline との差分、推奨アクションの期限根拠を追加します。

95. **Q: false positive が多い場合、どの順で調査しますか。**  
    A: fixture/adapter 入力、スキーマ範囲、threshold 境界、asset vulnerability、maintenance history、実地点検ラベルとの対応、evidence 文言の順で確認します。

96. **Q: false negative が出た場合、どのような欠損が疑われますか。**  
    A: 必要な signal が未取得、baseline が不適切、threshold が高すぎる、asset metadata が粗い、visual/thermal の sampling が不十分、risk category が不足している可能性があります。

97. **Q: adapter contract を破る変更をどうリリースしますか。**  
    A: docs と schema を先に更新し、互換 adapter または migration path を用意し、old/new fixture を並行テストし、risk engine への影響を regression で確認してから切り替えます。

98. **Q: 現場データを扱う場合の security/privacy 上の注意点は何ですか。**  
    A: 画像、位置、設備稼働、入退室に近い情報はセンシティブです。最小収集、匿名化、ローカル保存、アクセス制御、artifact の公開範囲、ログ出力を設計する必要があります。

99. **Q: SignalTwin を SaaS 化する場合、最初に分離すべき boundary は何ですか。**  
    A: tenant/project、building/asset、adapter ingestion、baseline store、risk calculation job、artifact storage、API response の boundary です。

100. **Q: シニアエンジニアとして現状コードに最初に入れる改善は何ですか。**  
     A: 検証済み Pydantic model を pipeline 中央で dict に潰さない設計に寄せます。`AdapterOutput`、`NormalizedScenario`、API/dashboard builder で型付き model を保持し、`model_dump()` はファイル出力や HTTP response など serialization edge に限定します。
