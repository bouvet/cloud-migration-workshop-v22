## Oppgave 1
Lag en AWS Lambda-funksjon som kan lytte på filer som blir lastet opp til en S3-bøtte.
Lambda-funksjonen skal bruke "upload eventet" til å lese den opplastede filen fra S3-bøtta
Den skal så skrive innholdet i filen til en DynamoDB-tabell.

1. Opprett en S3 bøtte (med default settings)
2. Opprett en DynamoDB tabell (med default settings og id som partition key)
3. Opprett en AWS Lambda funksjon (bruk Python)
   1. Lim inn kode
   2. Oppdater variabelnavn for DynamoDB tabell navn.
   3. Legg til IAM policy på Lambda-funksjonens IAM rolle:
      1. `AmazonS3ReadOnlyAccess`
      2. `AmazonDynamoDBFullAccess`
   4. Legg til Lambda Trigger (lytt på S3 "All object create events")
   5. Deploy Lambda funksjon
4. Test applikasjonen din ved å laste opp en fil til S3-bøtta og se at innholdet blir skrevet til DynamoDB-tabellen din.


## Oppgave 2
Opprett en API Gateway som kan kalle på en Lambda funksjon. Denne Lambda funksjonen skal returnere ett objekt basert på en id fra tabellen du opprettet i oppgave 1.

1. Lag en ny AWS Lambda-funksjon
   1. Lim inn kode for oppgave 2
   2. Oppdater variabelnavn for DynamoDB tabell navn.
   3. Legg til IAM policy på Lambda-funksjonens IAM rolle:
      1. `AmazonDynamoDBReadOnlyAccess`
2. Opprett en HTTP API Gateway.
   1. Legg til en Lambda-integrasjon I API Gateway.
   2. Den skal peke på din nye Lambda-funksjon.
   3. Bruk en HTTP GET metode
   4. Legg til den resource path-en du ønsker, inkludert et path parameter som heter `id` f.eks: `/birds/{id}`.
3. Test endepunktet ved å kalle URL-en som er vist i API Gateway-en.


## "shameless reklame" for videoer som gir svar på oppgavene:
- [Lambda trigger on s3 upload event](https://www.youtube.com/watch?v=-x3A4DG0Kjw)
- [API Gateway with lambda integration](https://www.youtube.com/watch?v=TzbImff5KO0)
