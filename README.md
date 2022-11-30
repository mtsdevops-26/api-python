# bullhorn-api-example-python
Este é um exemplo de aplicativo Python que demonstra um uso muito simples da API Bullhorn REST de um aplicativo da Web.

O maior obstáculo inicial para os desenvolvedores normalmente é fazer com que a autenticação OAuth funcione corretamente, portanto grande parte desta amostra é dedicada a isso.

Você precisará de uma chave de parceiro OAuth e um segredo para executar o aplicativo de amostra com êxito.

Esta amostra usa uma pequena estrutura da Web em Python, web.py, para ativar um aplicativo da Web para demonstrar o fluxo completo de redirecionamento, autenticação e redirecionamento OAuth.

Existem quatro arquivos de origem:

api.py - Funções utilitárias para fazer login na API REST e fazer chamadas para ela
oauth.py - Funções utilitárias para fazer chamadas de autenticação OAuth
web_utils.py - Algumas funções gerais do utilitário da Web
api_example.py - O código principal do aplicativo de amostra. Gira e configura o aplicativo Web e implementa manipuladores de solicitação para OAuth e chamadas de API de amostra.
