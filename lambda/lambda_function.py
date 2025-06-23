def handler(event, context):
    print("Evento S3 recebido:", event)
    return {
        "statusCode": 200,
        "body": "Evento S3 processado com sucesso!"
    }
