
1. b,d
2. c
3. a
4. a->b  secret manager は自動ローテーション対応
5. b
6. d
7. b,d
8. a->d 読み取りはレプリカ！作業量が要件でなければマルチAZのAuroraレプリカが最適
9. b
10. d
11. b
12. b
13. d->c lamdaは15分以内の処理だけ！
14. b->a,c サードパーティの証明書は基本手動
15. d
16. a,b,c ->b,c,f　Aのキーポリシー、Aのバケットポリシー、BのインスタンスIAMロール
17. c
18. b
19. c
20. d
21. b
22. d DLM とのちがい　DLMはEC2だけのサービス
23. c glue opensearch 
24. a->a,e controll tower のデータレジデンシーガードレールでリージョン制限できる
25. c
26. a->c 最強はinstance saving(インスタンス指定ガチガチで72%)
27. a
28. d
29. d->a fargate lamda 節約ならcompute saving 年間コミット　
30. b,c->b,d S3 (PutObject) → EventBridge (ルール) → Step Functions (ステートマシン起動)
31. c,d 
32. c
33. d->c AWSSysteManager=SSM そのなかの SessionManager.を使うことが踏み台が割の推奨
34. d
35. d
36. b
37. d
38. b->c pull 方ならSQS一択、注意すべきは何時間おきに取得するか書いてあるかだけ
39. c
40. a
41. b
42. a
43. a
44. d->c easy
45. c->a サードパーティならssm run command
46. c
47. a
48. c
49. b
50. a