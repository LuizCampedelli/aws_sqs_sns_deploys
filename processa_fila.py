import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/322709898531/Ada_Fila'

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,  # Número máximo de mensagens a serem recebidas
    WaitTimeSeconds=10  # Tempo de espera
)

# Verifica se há mensagens e exibe a primeira
if 'Messages' in response:
    message = response['Messages'][0]
    print("Mensagem recebida:", message['Body'])


    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
    print("Mensagem processada e excluída.")
else:
    print("Nenhuma mensagem encontrada na fila.")
