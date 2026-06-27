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

