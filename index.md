# 間違える問題

## 外部ベンダーが使用する資格情報は、そのベンダー専用に制限
- アクセスを委任するためには、クロスアカウントアクセス権限とIAMロールの設定が不可欠です。

## シンプルなSQLステートメントを用いてAmazon S3バケット内のオブジェクトをフィルタリング
- クエリ結果の保存先のS3バケットと入力データとなるS3バケットを設定したクエリエディタを作成

## セキュリティのAWS Foundational Security Best Practices (FSBP) 標準に準拠していないAWSアカウントが存在する場合、それを把握
- 既存アカウントがAWS Foundational Security Best Practices 標準から逸脱していないかを監査するためには、AWS Security Hub Cloud Security Posture Management (CSPM) を利用します。


## ニアリアルタイム
- 「一日中継続して数十〜数百のジョブが実行されること」と「ニアリアルタイムに処理すること」が求められています。これは「Amazon EMRクラスターの利用が最適となるケース」に合致します。


## AWS SAMを活用したCloudFormationテンプレートを作成し、Amazon S3バケットを利用してデプロイを実施
- CloudFormationテンプレート内でAWS::Serverless Transform設定において使用するAWS SAMのバージョンを指定することが求められます。


## 既存のWindowsアカウント情報を用いてAWS環境へのユーザー認証を行い、AWSマネジメントコンソールを利用できるようにする必要
- IAMダッシュボードとAWS Directory Service Connectを利用したシングルサインオン機能というものは存在しません


## このアプリケーションを東京リージョンから東南アジアに展開することになり、データ処理がシンガポールリージョンにも自動的に複製されるレプリケーション構成を実現する必要があります。
- DynamoDB Streamsを有効にする必要があります。これにより、東京リージョンのDynamoDBテーブルにおけるデータの更新が発生した際に、シンガポールリージョンのDynamoDBテーブルへと自動的にレプリケーションされます。



## AWSに移行するデータベースに対して、同一リージョン内でのできる限り高い可用性とスケーラビリティを確保する構成が求められています
- Amazon Auroraにおいて「マルチAZ配置を有効化する」という単一のチェックボックスやボタンといった操作は、標準的なRDS（MySQLやPostgreSQLなど）とは異なり、直接的には存在しません。



## WorkSpacesを利用するために新規にIAMユーザーを人数分設定するのは面倒
- AD Connectorは、簡易的にIAMとオンプレミスのMicrosoft Active Directoryとの統合を実現する機能です。AD ConnectorとMicrosoft Active Directoryが統合されるとMicrosoft Active Directoryユーザーに対するAWSサービス認証が可能となります。



## Simple AD, Microsoft Active Directory
- Microsoft Active Directory が本物。 simple AD は互換品
- **AD Connector：** 新しくは作らない。**「すでに社内にある本物」をそのままAWSから使う**


## CloudFormation スタックセット
- スタックセットを使うと、その面倒な「アカウントの切り替え作業」を**AWS（CloudFormation）側が裏で全自動でやってくれます。**


## 平均ゴール数や平均パス数など、さまざまなプレーに関する詳細なデータを収集し、レポートを作成して、サッカーのプレミアリーグファンやスポーツメディアに提供します。試合日には世界中のユーザーから20万件以上のクエリが発生する見込みです。
- CloudFrontによる配信を実施する。
- ElastiCacheはインメモリデータベースであり、高速なデータ処理を実現しますが、コンテンツ配信処理の機能は有していません。



## S3ゲートウェイエンドポイントを利用して、Amazon EC2インスタンスからS3バケットにアクセスする。
- 経路を作るのはVPCエンドポイント、それをS3側で受け入れる/制限するのがバケットポリシー
- S3用のゲートウェイ型VPCエンドポイント

![](assets/Pasted%20image%2020260627123141.png)


## AWS のEC2までの構図
![](assets/Pasted%20image%2020260627123111.png)


## Route53 
- 純粋なトラフィック配分なら加重ルーティング
- レイテンシーマルチリージョンで最速のリージョンへ
- フェイルオーバー障害時にバックアップへ切替
- シャッフルシャーディングはDDoSを防げるAWSの仕組みでRoute53の標準機能



## VPCサイト間接続
- EC2が `web.internal.example.com`、DBが `db.internal.example.com` だとします。このとき、オンプレのリゾルバーに `web...` と `db...` を個別に登録する必要はありません。共通の末尾である **`internal.example.com` というゾーンに対して1つだけ転送ルールを書けば、その配下は全部まとめてインバウンドエンドポイントに飛びます**。
![](assets/Pasted%20image%2020260627125538.png)


## SCPとIAM/OU
- アカウントをまとめる OU

![](assets/Pasted%20image%2020260627130702.png)

- SPC and IAMポリシー
![](assets/Pasted%20image%2020260627130737.png)
- AWS Organizations は、前回話した通り「**複数のAWSアカウントを組織として束ねる**」土台
- AWS Control Tower は、その上に乗る「**マルチアカウント環境を、ベストプラクティスに沿って自動でセットアップ・管理してくれる**」
- AWS Security Hub は、「**各アカウントのセキュリティ状態を一箇所に集めて、ベストプラクティスに沿っているか自動でチェック・採点する**」



## データへの高速アクセスを可能にすることが必要です。また、ゲームデータを維持するためには、アプリケーションを再起動後にもデータがディスクに永続化
- アプリケーションを再起動した後でもデータがディスクに永続化される必要があります。Amazon ElastiCache Redis OSSクラスターをデプロイ



## Amazon EC2インスタンスにホストされたActiveMQを用いてキューメッセージを送信し、その後、別のAmazon EC2インスタンス上で動作するコンシューマーアプリケーションがメッセージを処理
![](assets/Pasted%20image%2020260627132546.png)
- オンプレや既存システムを、コードを変えずにAWSへ移行(リフト&シフト)したいとき → MQ。
- ゼロからAWS上で新規に作るとき → SQS
![](assets/Pasted%20image%2020260627132533.png)
- なぜEBSではなくEFSなのかというと、EBS（普通のディスク）は1つのAZ・基本1つのEC2に紐づくのに対し、EFSは複数AZ・複数EC2から共有できるからです。「AZをまたいで同じデータを使いたい」要件には、EFSが向いています。
- EFSのデータ実体は「どのAZにも無い」のではなく、「AWSが裏で複数AZに冗長保存している」(だからデータ自体はAZ障害に強い)。それでもマルチAZで組むのは、データのためではなく、**各AZのEC2がアクセスするための入り口(マウントターゲット)を、使う全AZに用意する必要があるから**。


## フェールオーバー
- 「アクティブ/アクティブ」ラウンドロビン
- 「アクティブ/パッシブ」フェイルオーバー



## Cognito
- Cognitoの出番ではありません。Cognitoは「アプリにログインする大勢の人間」を捌く
- アクセスしてくるのが「人間」ではなく「**別のシステム/アプリケーション**」ならIAMロールでこれが満たせる


## S3解析の早見
- EMR（Elastic MapReduce）は、ひとことで言うと **大量データを複数台のサーバーで分散処理するための「ビッグデータ処理基盤」をマネージドで提供するサービス**
![](assets/Pasted%20image%2020260627134641.png)


## 引っかけ

- 標準RDSの高可用性 → 「**マルチAZ配置を有効化**」（スタンバイを別AZに、機能としてオン）。
- Auroraの高可用性 → 「**別AZにAuroraレプリカを配置**」（レプリカを置く構成にする。ストレージは元々マルチAZ）。
- 選択肢を読むときのコツは、**「Aurora」なのに「マルチAZ配置を有効化する」というRDSの言い回しが出てきたら警戒する**ことです。
- 「**Auroraはストレージを手動で拡張する**」→ 誤り。Auroraのストレージは完全自動。手動拡張が要るのは通常のRDSの方（それもAuto Scaling設定できるが）。
- 「**DynamoDBのAuto Scalingはサーバー台数を増やす**」→ 誤り。増減するのはキャパシティ(RCU/WCU)。

## AWS FireWall Manager

## AWS 側にはアカウントがない
- AD Connectorを利用してオンプレミス環境のMicrosoft Active Directoryと連携することで、Microsoft Active Directoryユーザーに対してWorkSpacesを利用する権限を付与する。


## リザーブド
・EC2リザーブドインスタンス
・RDSリザーブドインスタンス
・ElastiCacheリザーブドキャッシュノード
・DynamoDBリザーブドキャパシティ
・Redshiftリザーブドノード


## ほぼStepFunction
- 複数のLambda関数を用いてデータ処理を行う必要があります。


## RAG
- Amazon OpenSearch Service Amazon S3 Vectors Amazon DocumentDB
![](assets/Pasted%20image%2020260627153508.png)


##  クレカの不正検出
![](assets/Pasted%20image%2020260627154242.png)

## リアルタイム保存
- Managed Flinkリアルタイム流れるデータをその場で処理・分析(気象データなど)



## EKS
- コントロールプレーンはAWSの範囲でユーザーは触らない
- インターフェースVPCエンドポイントを構成
![](assets/Pasted%20image%2020260627155610.png)

## Lake Formation
- EMRやAthenaでS3のデータを分析するとき、「このユーザーはこのテーブルのこの列だけ見ていい」
- ### AWS Data Exchange「**外部のデータプロバイダーが提供するデータセットを、AWSマーケットプレイス経由でサブスクライブして使えるサービス**」
![](assets/Pasted%20image%2020260627164151.png)


## KMS
- 「**KMSで暗号化されたリソース（SNS/SQS/S3など）にアクセスしたい**」という問題が出たら、**アクセスする側のIAMロールにKMS権限も必要**
![](assets/Pasted%20image%2020260627185950.png)


- Amazon TranscribeのPIIリダクション機能を活用します。この機能を有効化して、Amazon Transcribeの文字起こしジョブを設定することで、顧客個人を特定できる情報を自動的に除去する


## DynamoDBでは以下の2つのキャパシティモードが利用可能です。
・オンデマンド
・プロビジョンド (デフォルト、無料利用枠の対象
- 削除検知してstream firehose → s3移動でコスト下げられる
![](assets/Pasted%20image%2020260627191831.png)

- 「**定期実行・スケジュール**」というキーワードが出たら、**EventBridge**が必ずセット




![](assets/Pasted%20image%2020260627195704.png)



## EKS scale
![](assets/Pasted%20image%2020260627202303.png)


## 過程で複数のインスタンス間での通信が頻繁に行われます。このEC2インスタンスを用いた作業の効率化が求められています。
- 「インスタンス間通信が多い」というキーワードが出たらクラスタープレイスメントグループを思い出すと良いです。
- クラスタープレイスメントグループを設定した上で、M5インスタンス群を起動する。


**Savings Plansの種類は3つ**あり、その1つがEC2 Instance Savings Plans。
- **Compute Savings Plans** — 最も柔軟。インスタンスファミリー・リージョン・OS・テナンシー問わず適用。Fargate、Lambdaにも適用。割引率は最大66%。
- **EC2 Instance Savings Plans** — 特定リージョンの**特定インスタンスファミリー**にコミット。柔軟性は下がるが割引率が高い（最大72%）。
- **SageMaker Savings Plans** — SageMaker向け。


- secret manager は自動ローテーション対応
- 読み取りはレプリカ！作業量が要件でなければマルチAZのAuroraレプリカが最適
- lamdaは15分以内の処理だけ！
- サードパーティの証明書は基本手動
- Aのキーポリシー、Aのバケットポリシー、BのインスタンスIAMロール
- controll tower のデータレジデンシーガードレールでリージョン制限できる
- 最強はinstance saving(インスタンス指定ガチガチで72%)
- fargate lamda 節約ならcompute saving 年間コミット　
- S3 (PutObject) → EventBridge (ルール) → Step Functions (ステートマシン起動)
- AWSSysteManager=SSM そのなかの SessionManager.を使うことが踏み台が割の推奨
- pull 型ならSQS一択、注意すべきは何時間おきに取得するか書いてあるかだけ
- サードパーティならssm run command


## 総さらい

# 1

![](assets/Pasted%20image%2020260628115858.png)
![](assets/Pasted%20image%2020260628115907.png)

**決め手:** 「1TB超/日の大量データをS3に貯めて分析」→ S3上のデータをそのままSQLで分析する **Redshift Spectrum**（またはAthena）が定石。



![](assets/Pasted%20image%2020260628115928.png)
![](assets/Pasted%20image%2020260628120036.png)
  **決め手:** 「注文を分類して振り分け」+「12時間以内に処理」+「費用対効果」→ **SNSのメッセージフィルタリング**で種類別にSQSキューへ振り分け、各キューをバックエンドがpullで処理。これが定石パターン。


![](assets/Pasted%20image%2020260628120102.png)
![](assets/Pasted%20image%2020260628120110.png)
**決め手:** 「別アカウントのサードパーティが自社EC2にアクセス」→ **クロスアカウントIAMロール**。アクセスを委任する方向を正確に意識する。


![](assets/Pasted%20image%2020260628120122.png)
![](assets/Pasted%20image%2020260628120132.png)
**決め手:** 「API Gatewayの呼び出し元に権限管理」→ **IAMポリシー**でAPIへのアクセス制御。



![](assets/Pasted%20image%2020260628120236.png)
![](assets/Pasted%20image%2020260628120242.png)
**決め手:** 「S3内のデータを分類・分割する」→ **Glueクローラー**。S3をスキャンしてスキーマを自動検出し、データカタログに登録＝分類・分割が役割。


![](assets/Pasted%20image%2020260628120254.png)
![](assets/Pasted%20image%2020260628120304.png)
  **決め手:** 「スケーラブル・高可用性・MySQLの読み取りレイテンシー削減」→ EC2側はALB+ASG、DB側はAuroraクラスター（同一リージョン内のリーダーレプリカ）。
ノートに書いた通り、Auroraに「マルチAZ配置を有効化」という操作は存在しない。これは標準RDSの言い回し。Auroraで高可用性を出すには「別AZにAuroraレプリカを配置」。



![](assets/Pasted%20image%2020260628120318.png)
![](assets/Pasted%20image%2020260628120326.png)
**決め手:** 「CPUリソースを**設定して管理**する必要がある」→ **ECS + EC2起動タイプ**。EC2インスタンスのCPUファミリーを自分で選んで管理できる。**ECS + EC2** → インスタンスタイプ・CPUファミリーを自分で管理したい、GPUが必要、細かいリソース制御が必要


![](assets/Pasted%20image%2020260628120337.png)
![](assets/Pasted%20image%2020260628120345.png)
**引っかけのポイント:** 「RDS読み取りパフォーマンスが低下」という文言でRDS側を疑わせる。でも原因はEC2。問題文の「〜することで」という因果関係を正確に追うことが大事。



![](assets/Pasted%20image%2020260628120356.png)![](assets/Pasted%20image%2020260628120402.png)
**決め手:** デッドレターキューは**Lambda関数に追加する**もの。SQSに追加するものではない。


# 2
![](assets/Pasted%20image%2020260628120438.png)![](assets/Pasted%20image%2020260628120444.png)
**決め手:** 「Lustreクライアントから接続可能な共有ストレージ」→ **Amazon FSx for Lustre** 一択。名前そのまま。


![](assets/Pasted%20image%2020260628120458.png)
![](assets/Pasted%20image%2020260628120506.png)
  **決め手:** 「リアルタイム処理不要・数分の遅延OK・コスト最小」→ **Firehose**。Kinesis Data Streamsは不要。


![](assets/Pasted%20image%2020260628120518.png)![](assets/Pasted%20image%2020260628120525.png)
**決め手:** 「特別なハードウェア不要・データ量大きくない・コスト最適・数分以内」→ **Lambda**。シンプルな処理にはLambdaが最安。




![](assets/Pasted%20image%2020260628120536.png)![](assets/Pasted%20image%2020260628120549.png)
  
**決め手:** 「リアルタイム処理」+「形式変換」+「コスト効率良いデータレイヤーに保存」→ **Kinesis Data Streams → Flink（変換）→ Firehose → Lambda変換 → S3**


![](assets/Pasted%20image%2020260628120558.png)![](assets/Pasted%20image%2020260628120603.png)
  

**決め手:** 「12:00〜13:30のピーク時間帯が決まっている」→ **スケジュールドスケーリング**で事前にスケールアップ。ここは両方同じなので差分で判断。ECSのEC2起動タイプでALBと連携する場合、**ELBヘルスチェックの有効化**が必須。これがないと不健全なインスタンスにトラフィックが流れ続ける。キャパシティプロバイダーはASGを指定して作成するもので、ASGに「アタッチする」という表現が不正確。



![](assets/Pasted%20image%2020260628120615.png)![](assets/Pasted%20image%2020260628120622.png)
**決め手:** 「プライベートサブネットのEC2がソフトウェア更新（=インターネットへのアウトバウンド）できない」→ NATゲートウェイ＋踏み台サーバー。



![](assets/Pasted%20image%2020260628120637.png)
![](assets/Pasted%20image%2020260628120651.png)
  

**決め手:** SCPは「使える権限の上限（ガードレール）」を定義するもので、それ自体が権限を付与するわけではない。



![](assets/Pasted%20image%2020260628120704.png)![](assets/Pasted%20image%2020260628120710.png)
  

**決め手:** 「変換」と「リダイレクト」は別物。


![](assets/Pasted%20image%2020260628120722.png)![](assets/Pasted%20image%2020260628120728.png)
  

**決め手:** 「毎週定期的にDynamoDB→S3エクスポート」→ **Glue**。ETLジョブのスケジュール実行が得意。



![](assets/Pasted%20image%2020260628120738.png)![](assets/Pasted%20image%2020260628120746.png)
  

**決め手:** 「25,000 IOPS・コスト効率」→ **EC2サイズアップ + RAID0**。



![](assets/Pasted%20image%2020260628120759.png)![](assets/Pasted%20image%2020260628120806.png)
  

**決め手:** 「CPU・メモリ・ストレージ・ENIを共有してはいけない」＝**ノードレベルでの完全分離**が必要 → Taint/Toleration + Node Affinity で特定PodをノードにピンどめしてNodeを専有させる。



![](assets/Pasted%20image%2020260628120818.png)![](assets/Pasted%20image%2020260628120825.png)
  

**決め手:** 「S3にファイル保存→変換処理」→ **S3イベント通知→Lambda直接**。Firehoseは不要。


# 3
![](assets/Pasted%20image%2020260628120847.png)
![](assets/Pasted%20image%2020260628120855.png)
**決め手:** 「永続化」+「データパーティショニング」→ **Redis（クラスターモード有効）**。





![](assets/Pasted%20image%2020260628120905.png)![](assets/Pasted%20image%2020260628120910.png)
  

**決め手:** 「NASストレージ」の置き換え＋「複数AZのEC2から共有アクセス」→ **EFS**。RDS MySQLは不正解。

![](assets/Pasted%20image%2020260628120921.png)![](assets/Pasted%20image%2020260628120927.png)
  

**決め手:** 「S3内のPII（個人情報）を自動検出」→ **Amazon Macie**一択。



![](assets/Pasted%20image%2020260628120940.png)
![](assets/Pasted%20image%2020260628120947.png)
  

**決め手:** 「異常がない場合は均等に利用」→ **アクティブ／アクティブ**。

ノートに書いてある通りそのままです。



![](assets/Pasted%20image%2020260628120958.png)![](assets/Pasted%20image%2020260628121004.png)
  

**決め手:** 「別アカウントのサードパーティが自社EC2にアクセス」→ **クロスアカウントIAMロール**。先ほどの問題と同じパターン。**CognitoがなぜダメかはCognitoの役割:**  
ノートに書いてある通り「Cognitoは大勢の人間ユーザーを捌くもの」。アクセスしてくるのが「人間」ではなく「別システム/アプリケーション」ならIAMロールで対応する。



![](assets/Pasted%20image%2020260628121016.png)![](assets/Pasted%20image%2020260628121024.png)
  

**決め手:** 「読み取り専用・シンプルモデル・予測不可能なトラフィック」→ **Memcached**。

さっきの問題と真逆のパターンです。



![](assets/Pasted%20image%2020260628121034.png)![](assets/Pasted%20image%2020260628121041.png)
  

**決め手:** 「東京→シンガポールへ自動レプリケーション」→ **DynamoDB Streams有効化 ＋ グローバルテーブル設定**。




![](assets/Pasted%20image%2020260628121054.png)
![](assets/Pasted%20image%2020260628121101.png)

**決め手:** 「Organizations全体でセキュリティグループルールを一元管理・自動検出」→ **AWS Firewall Manager**。



![](assets/Pasted%20image%2020260628121111.png)
![](assets/Pasted%20image%2020260628121117.png)
「Auroraクラスターを作成しマルチAZ配置を有効化する」→ 存在しない操作なので不正解。
- 標準RDSの高可用性 → 「マルチAZ配置を有効化」
- **Auroraの高可用性 → 「別AZにAuroraレプリカを配置」**


![](assets/Pasted%20image%2020260628121128.png)![](assets/Pasted%20image%2020260628121136.png)
  

**決め手:** 「既存のオンプレMicrosoft ADをそのまま使う」→ **AD Connector**。


![](assets/Pasted%20image%2020260628121149.png)
![](assets/Pasted%20image%2020260628121202.png)
- EC2・RDSはインターネットと直接通信しない → **プライベートサブネット**
- EC2からソフトウェア更新のためインターネットへアウトバウンド → **NATゲートウェイ（パブリックサブネット）**
- 可用性向上 → **マルチAZ（2つのAZ）**





![](assets/Pasted%20image%2020260628121240.png)![](assets/Pasted%20image%2020260628121247.png)
  

**決め手:** 「オンプレ→AWS方向のDNS名前解決」→ **インバウンドエンドポイント＋オンプレDNSリゾルバーの転送設定**。





# 4
![](assets/Pasted%20image%2020260628121309.png)![](assets/Pasted%20image%2020260628121318.png)
  

**決め手:** 「大量の読み取りクエリで処理速度低下・コスト最適」→ **RDSリードレプリカ、インスタンスタイプは変更しない**。



![](assets/Pasted%20image%2020260628121329.png)
![](assets/Pasted%20image%2020260628121335.png)
  

**決め手:** 「エラーが他の処理に影響しない」+「予測不可能なリクエスト数」+「管理オーバーヘッド最小」→ **SQS + Lambda**。




![](assets/Pasted%20image%2020260628121345.png)![](assets/Pasted%20image%2020260628121352.png)
  

**決め手:** 2つのポイントで絞る。「PutObject vs GetObject」と「バケットポリシー vs IAMポリシー」。




![](assets/Pasted%20image%2020260628121402.png)
![](assets/Pasted%20image%2020260628121413.png)
  

**決め手:** DynamoDBはセキュリティグループが存在しない。

**正解2つの理由:**

- **LambdaにDynamoDB操作のIAMロール（正解）** → DynamoDBへのアクセスはIAMで制御。これは必須。
- **RDS側のSGインバウンドでLambdaのSGを許可（正解）** → LambdaがRDSに接続するにはRDS側のSGで「Lambdaからの接続」を許可する必要がある。接続を受け入れる側（RDS）のインバウンドルールを開ける。




![](assets/Pasted%20image%2020260628121453.png)
![](assets/Pasted%20image%2020260628121500.png)

**決め手:** 「オンプレ+AWSにまたがる分散アーキテクチャの処理プロセス・データ連携」→ **Step Functions + SQS**。





![](assets/Pasted%20image%2020260628121512.png)![](assets/Pasted%20image%2020260628121517.png)
  

**決め手:** SGの方向（インバウンド/アウトバウンド）とポート番号（22/80）を正確に読む。

**接続の流れ:**

```
社内PC → (SSH:22) → 踏み台サーバー → (SSH:22) → アプリケーションサーバー
```



![](assets/Pasted%20image%2020260628121526.png)![](assets/Pasted%20image%2020260628121532.png)
**決め手:** 2つの違いを整理する。「IAMロール vs リソースベースポリシー」と「lambda.amazonaws.com vs events.amazonaws.com」。

**プリンシパルの違い:**

- **events.amazonaws.com（正解）** → EventBridgeのサービスプリンシパル。EventBridgeがLambdaを呼び出す権限を付与する場合はこれ。
- **lambda.amazonaws.com（不正解）** → Lambdaのサービスプリンシパル。LambdaがIAMロールを引き受ける場合（Lambda実行ロール）に使うもの。



![](assets/Pasted%20image%2020260628121542.png)![](assets/Pasted%20image%2020260628121548.png)
  

**決め手:** 「順番に処理」→ **SQS FIFOキュー**。





# 5
![](assets/Pasted%20image%2020260628121611.png)![](assets/Pasted%20image%2020260628121618.png)
**決め手:** 「複数ノードから1桁ミリ秒単位のアクセス」→ **S3 Express One Zone**。




![](assets/Pasted%20image%2020260628121629.png)![](assets/Pasted%20image%2020260628121635.png)
  

**決め手:** 「特定IPからの不正リクエストをブロック」→ **ウェブ層（パブリックサブネット）のネットワークACL**。






![](assets/Pasted%20image%2020260628121644.png)![](assets/Pasted%20image%2020260628121652.png)


**決め手:** SSL証明書のマッピング先は**Route53ではなくAPI Gateway**。







![](assets/Pasted%20image%2020260628121701.png)![](assets/Pasted%20image%2020260628121709.png)

  

**決め手:** EKSのプライベートアクセス制限に必要な3点セット。ノートの「EKS」項目そのもの。




![](assets/Pasted%20image%2020260628121718.png)![](assets/Pasted%20image%2020260628121726.png)
  

**決め手:** 「既存Microsoft ADでAWSコンソールにSSO + サードパーティアプリ連携」→ **IAM Identity Center + Directory Serviceの信頼関係**。






![](assets/Pasted%20image%2020260628121734.png)![](assets/Pasted%20image%2020260628121740.png)

  

**決め手:** 「処理が間に合わない・未処理が発生・自動再試行」→ **SQSをバッファに挟む**。





![](assets/Pasted%20image%2020260628121747.png)![](assets/Pasted%20image%2020260628121754.png)
  

**決め手:** NLB→EC2のトラフィックフローに沿って、各層で正しい送信元を許可する。

**正解2つの構成:**

```
クライアント（特定IP）→ NLBのSG（特定IPからポート22許可）
→ EC2のSG（NLBのSGからポート22許可）
```

- **NLBのSGで特定IPからTCP22許可** → 外部クライアントからNLBへの入り口を開ける
- **EC2のSGでNLBのSGからTCP22許可** → NLBからEC2への通信を許可。送信元はNLBのSG





![](assets/Pasted%20image%2020260628121803.png)![](assets/Pasted%20image%2020260628121809.png)
**一言で覚える:**

- 外部共有 → Data Exchange
- データレイク内の機密検出 → Glue Sensitive Data Detection
- Secrets Manager → シークレット管理（検出ではない）






![](assets/Pasted%20image%2020260628121817.png)![](assets/Pasted%20image%2020260628121823.png)

  

**決め手:** 「LambdaがDirect Connect経由でオンプレDBにアクセス」→ **LambdaをVPC内に配置**。







![](assets/Pasted%20image%2020260628121831.png)![](assets/Pasted%20image%2020260628121837.png)
  

**決め手:** 「ディスクI/OとIOPSがボトルネック」→ ストレージ側を強化する2択。





![](assets/Pasted%20image%2020260628121845.png)![](assets/Pasted%20image%2020260628121851.png)
**決め手:** 「SFTPクライアントでS3にアップロード」→ **AWS Transfer for SFTP**。








![](assets/Pasted%20image%2020260628121859.png)![](assets/Pasted%20image%2020260628121905.png)

**決め手:** EC2がAWSリソースにアクセスする権限は**IAMロール**で付与。IAMユーザーではない。




# 6
![](assets/Pasted%20image%2020260628121935.png)![](assets/Pasted%20image%2020260628121942.png)
**不正解（SNSトピックにアクセス許可ポリシー）の理由:**  
LambdaがSNSにアクセスするには、Lambda側（実行ロール）に権限を付与するのが正しい。SNS側のリソースポリシーで許可する方法も技術的には可能ですが、「最小権限・ベストプラクティス」的にはLambdaの実行ロールにSNS publishを付与するのが正解。



![](assets/Pasted%20image%2020260628121952.png)
![](assets/Pasted%20image%2020260628122010.png)
**決め手:** 「数テラバイト・複雑なデータクレンジング・定期実行」→ **Glue + EventBridgeスケジュール**。Lambdaでは処理できない。




![](assets/Pasted%20image%2020260628122018.png)![](assets/Pasted%20image%2020260628122024.png)

**決め手:** 「複数リージョンのNLB・TCP/UDP・グローバルレイテンシー短縮」→ **AWS Global Accelerator**。



![](assets/Pasted%20image%2020260628122031.png)![](assets/Pasted%20image%2020260628122037.png)

  

**決め手:** 「NFS/SMBでS3データにアクセス」→ **Storage Gateway ファイルゲートウェイ**。







![](assets/Pasted%20image%2020260628122046.png)![](assets/Pasted%20image%2020260628122052.png)
  

**決め手:** 「不特定IPからのDDoS攻撃・最小限の労力」→ **Shield Advanced + SRT**。








![](assets/Pasted%20image%2020260628122100.png)![](assets/Pasted%20image%2020260628122107.png)
  

**決め手:** 「SFTPでデータ転送・最小1台・運用オーバーヘッド最小」→ **Transfer for SFTP + EFS** + **ASG(min=1, desired=1)**。





![](assets/Pasted%20image%2020260628122116.png)![](assets/Pasted%20image%2020260628122123.png)

**決め手:** 「SMBファイル共有→S3に集約」+「SQLで定期クエリ」→ **S3ファイルゲートウェイ + Athena**。







![](assets/Pasted%20image%2020260628122132.png)![](assets/Pasted%20image%2020260628122139.png)
  

**決め手:** 「オンデマンドキャパシティモード + Auto Scalingは矛盾」。





![](assets/Pasted%20image%2020260628122147.png)![](assets/Pasted%20image%2020260628122154.png)

  

**決め手:** 「データ量急増・503エラー・コンピューティング上限」→ **Kinesis Data Streamsでバッファ化してLambdaで処理**。





![](assets/Pasted%20image%2020260628122203.png)![](assets/Pasted%20image%2020260628122210.png)

  

これは直感に反する問題です。よく読むと納得できます。

**決め手:** 「ストレージが故障した場合のRTO1分未満」→ **EBSをそのまま使う**。





![](assets/Pasted%20image%2020260628122218.png)![](assets/Pasted%20image%2020260628122224.png)

  

**決め手:** 「証明書の安全な管理」+「ECSタスクからのアクセス」→ **Secrets Manager + ECSタスクロール**。




![](assets/Pasted%20image%2020260628122232.png)![](assets/Pasted%20image%2020260628122238.png)
**決め手:** 「アップロード/ダウンロードサイト」にS3静的ウェブサイトは使えない。





![](assets/Pasted%20image%2020260628122247.png)![](assets/Pasted%20image%2020260628122253.png)


**決め手:** 「CloudFront経由で特定ユーザーのみにコンテンツ配信」→ **OAC + CloudFront署名付きURL**。





# 3minチェック


---

**方向・対象を間違えやすい系**

- SGは「受け取る側のインバウンド」を開ける
- NLB経由→EC2のSGにはNLBのSGを指定（クライアントIPではない）
- クロスアカウントアクセス→自社側にロールを作り相手にAssumeRoleさせる
- EventBridge→Lambda呼び出し許可は`events.amazonaws.com`のリソースベースポリシー

**Aurora引っかけ**

- Auroraに「マルチAZ配置を有効化」は存在しない→見たら即脱落
- Auroraの高可用性=別AZにレプリカを配置
- グローバルDB=別リージョン展開の時だけ

**サービス役割の混同**

- DynamoDBにSGは存在しない→アクセス制御はIAMのみ
- CloudFrontはDB前段に置けない
- Configは監査、STSは一時キー発行、権限付与はIAMのみ
- GuardDuty=脅威検出、Macie=S3のPII検出
- DataSync=一方向転送、Storage Gatewayファイルゲートウェイ=継続的なNFS/SMBファイル共有
- NATゲートウェイは必ずパブリックサブネット

**キャパシティ・スケーリング**

- DynamoDBオンデマンド+Auto Scalingは併用不可・無意味
- Lambda15分制限→大量データETLはGlue
- Flink=大量ストリーミング継続処理、Lambda=軽量単発

**証明書・暗号化**

- SSL証明書はRoute53ではなくAPI Gateway/ALB/CloudFrontにマッピング
- KMS暗号化リソースにアクセスする側のIAMロールにKMS権限も必要
- S3暗号化強制=`s3:PutObject`をバケットポリシーでDeny

**その他直前確認**

- FIFO=順番保証、標準=順序不問
- Redis=永続化あり、Memcached=純粋キャッシュのみ
- アクティブ/アクティブ=均等利用、アクティブ/パッシブ=待機
- Shield Advanced=DDoS+SRT、WAFはDDoSではなくアプリ層

---

落ち着いていってらっしゃい。今日の問題量こなせてるので大丈夫です。


