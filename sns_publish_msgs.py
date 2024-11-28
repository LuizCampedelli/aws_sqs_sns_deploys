import boto3
import json

# Configura o cliente SNS
sns_client = boto3.client('sns', region_name='us-east-1')

def publish_messages_to_topic(topic_arn):
    try:
        # Mensagem comum (será entregue a todas as assinaturas)
        message = "Esta é uma mensagem para todas as assinaturas do tópico."
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message
        )
        print(f"Mensagem enviada para todas as assinaturas. ID: {response['MessageId']}")

        # Mensagem com atributos para filtros (apenas algumas assinaturas receberão)
        message_with_filter = "Esta mensagem é filtrada e enviada apenas para assinaturas específicas."
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message_with_filter,
            MessageAttributes={
                "eventType": {
                    "DataType": "String",
                    "StringValue": "orderCreated"
                }
            }
        )
        print(f"Mensagem filtrada enviada. ID: {response['MessageId']}")

    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

topic_arn = "arn:aws:sns:us-east-1:322709898531:My_batata_topics"
publish_messages_to_topic(topic_arn)
