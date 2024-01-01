import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    # 任意代碼塊
    return func.HttpResponse("Hello, world!")