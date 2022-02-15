## Oppgave 1
Lag en AWS Lambda-funksjon som kan lytte på filer som blir lastet opp til en S3-bøtte.
Lambda-funksjonen skal bruke "upload eventet" til å lese den opplastede filen fra S3-bøtta
Den skal så skrive innholdet i filen til en DynamoDB-tabell.

> NB: Bruk gjerne eget navn på alle AWS-ressurser slik du lett kan skille dine resurser fra andres.

### Del 1: Opprett AWS ressurser
1. Opprett en S3 bøtte (med default settings). Navnet til S3-bøtta må være globalt unikt.
2. Opprett en DynamoDB tabell
   1. "Partition key" skal hete: `id` (la "Sort key" stå blankt).
   2. Ellers bare default settings på alt.

### Del 2: Opprett AWS Lambda funksjon
1. Opprett en AWS Lambda funksjon (bruk Python 3.9)
2. Fjern autogenerert kode og lim inn kode for [oppgave 1](./oppgave1.py).
3. I koden du nettopp limte inn; skriv inn navn på din DynamoDB-tabell (linje 8) og navn på din S3-bøtte (linje 9).
4. Gå til IAM, finn IAM-rollen med samme navn som din Lambda funksjon (dette er Lambda-funksjonens "execution role"). For at din Lambda funksjon skal få tilgang til din DynamoDB-tabell og S3-bøtte, må vi legge til følgende IAM-policies på denne IAM-rollen:
   1. `AmazonS3ReadOnlyAccess`
   2. `AmazonDynamoDBFullAccess`

### Del 3: Legg til AWS Lambda trigger
1. Gå tilbake til din AWS Lambda-funksjon.
2. Legg til Lambda Trigger:
   1. Velg `S3` og din S3-bøtte.
   2. Lytt på følgende event: `All object create events`.
   3. Les og huk av check-box for "Recursive invocation".
3. Gå tilbake til kode-vindu og klikk "Deploy" for å deploye alle endringer i din Lambda funksjon.

### Del 4: Test applikasjonen din!
1. Gå tilbake til S3-bøtten din.
2. Last opp [vedlagt fil](./birds.json) (eller en annen JSON fil).
3. Se at innholdet blir skrevet til DynamoDB-tabellen din.


## Oppgave 2
Nå skal vi opprette en API Gateway som kan kalle på en Lambda funksjon.
Denne Lambda funksjonen skal returnere ett objekt (basert på id-en) fra tabellen du opprettet i oppgave 1.

### Del 1: Opprett ny AWS Lambda funksjon
1. Lag en ny AWS Lambda-funksjon
2. Lim inn kode for [oppgave 2](./oppgave2.py)
3. I koden du nettopp limte inn; skriv inn navn på din DynamoDB-tabell (linje 5).
4. Finn IAM-rollen til denne Lambda funksjonen og legg til følgende IAM policy:
   1. `AmazonDynamoDBReadOnlyAccess`
5. Gå tilbake til Lambda-funksjonen og klikk "Deploy"

### Del 2: Opprett en API Gateway
1. Opprett en HTTP API Gateway:
   1. I "Step 1": Legg til en Lambda-integrasjon, denne skal peke på din nye Lambda-funksjon.
   2. I "Step 2": Velg GET som HTTP metode og definer ønsket path, inkludert et path parameter som heter `id` f.eks: `/birds/{id}`.
   3. I "Step 3": Fortsett uten å gjøre noen endrigner.
   4. I "Step 4": Klikk "Create".

### Del 3: Test API-et
1. Test endepunktet ved å kalle "Invoke URL" som er vist i API Gateway-en.

> NB: Husk å legge til resource path og id-en til et objekt som path parameter.


## Ekstra
1. Lag en AWS Lambda funksjon som kan trigges av meldinger på en SQS-kø.
2. Lag en AWS Lambda funksjon som kan sende meldinger til et SNS-topic.

## "shameless reklame" med løsningsforslag:
- Oppgave 1: [Lambda trigger on s3 upload event](https://www.youtube.com/watch?v=-x3A4DG0Kjw)
- Oppgave 2: [API Gateway with lambda integration](https://www.youtube.com/watch?v=TzbImff5KO0)
- Ekstraoppgave 1: [Lambda trigger on SQS messages](https://www.youtube.com/watch?v=eMknzzUqevQ)
- Ekstraoppgave 2: [Send meldinger fra en Lambda funksjon til et SNS-topic](https://www.youtube.com/watch?v=NrWkyzQMh4w)
