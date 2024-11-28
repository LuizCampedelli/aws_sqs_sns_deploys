import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/322709898531/Ada_Fila'

sqs = boto3.client('sqs', region_name='us-east-1')

response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Aluna xxx entregou o projeto'
)

print("Mensagem enviada com sucesso. ID da mensagem:", response['MessageId'])
