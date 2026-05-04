# Kafka + ZooKeeper + Kafka UI com Docker Compose

Este projeto sobe um ambiente local com:

- ZooKeeper
- Apache Kafka
- Kafka UI

## Estrutura do projeto

.
├── docker-compose.yml
└── README.md

## Requisitos

Antes de executar, tenha instalado:

Docker
Docker Compose

- Verifique as versões:

docker --version
docker compose version

## Serviços configurados
Serviço         Porta	        Descrição
ZooKeeper       2181	        Serviço usado pelo Kafka para coordenação
Kafka	        9092 / 29092	Broker Kafka local
Kafka UI	    8080	        Interface web para visualizar o cluster Kafka

## Como executar

Na pasta onde está o arquivo docker-compose.yml, execute:

docker-compose up -d --build

Esse comando irá baixar as imagens, criar os containers e iniciar os serviços em background.

- Verificar containers em execução
docker ps

- Você deve ver os containers:

zookeeper
kafka
kafka-ui


## Acessar o Kafka UI

Abra no navegador:

http://localhost:8080

Na interface, deve aparecer o cluster chamado:

local

- Verificar logs dos serviços

Para ver os logs de todos os serviços:

docker compose logs

Para acompanhar em tempo real:

docker compose logs -f

Logs individuais:

docker compose logs -f zookeeper
docker compose logs -f kafka
docker compose logs -f kafka-ui

## Teste básico de funcionamento
- Criar um tópico Kafka

Execute:

docker exec -it kafka kafka-topics --create \
  --topic teste-local \
  --bootstrap-server kafka:29092 \
  --partitions 1 \
  --replication-factor 1

Listar tópicos
docker exec -it kafka kafka-topics --list \
  --bootstrap-server kafka:29092

Saída esperada:

teste-local

## Testar envio e consumo de mensagens
- Enviar mensagem

Execute o producer:

docker exec -it kafka kafka-console-producer \
  --topic teste-local \
  --bootstrap-server kafka:29092

Digite uma mensagem, por exemplo:

Minha primeira mensagem no Kafka

Pressione Enter.

Para sair, use CTRL + C.

Consumir mensagem

Em outro terminal, execute:

docker exec -it kafka kafka-console-consumer \
  --topic teste-local \
  --bootstrap-server kafka:29092 \
  --from-beginning

Saída esperada:

Minha primeira mensagem no Kafka

## Para parar os containers:

docker-compose down

## Parar e remover volumes

- Caso queira limpar tudo:

docker compose down -v

## Observações importantes
O Kafka depende do ZooKeeper, por isso o serviço kafka usa depends_on.
O Kafka UI depende do Kafka e do ZooKeeper.
A porta 9092 é usada para acesso externo pelo host.
A porta 29092 é usada para comunicação interna entre containers.
O ambiente está configurado para uso local com apenas um broker Kafka.
A replicação foi definida como 1, pois existe apenas um broker no ambiente.