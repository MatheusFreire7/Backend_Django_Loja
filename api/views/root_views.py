from django.http import HttpResponse
from django.urls import reverse
import json

def root_view(request):
    api_info = {
        'message': 'Bem-vindo à API de loja!',
        'endpoints': {
            'Produtos': {
                'Descrição': 'Obter a lista de produtos e pesquisar produtos',
                'Métodos Permitidos': ['GET'],
                'Endpoints': {
                    'Listar Produtos': {
                        'URL': reverse('products'),
                        'Métodos Permitidos': ['GET'],
                    },
                },
            },
            'Usuários': {
                'Descrição': 'Gerenciar usuários',
                'Endpoints': {
                    'Registrar Usuário': {
                        'Descrição': 'Registrar um novo usuário',
                        'URL': reverse('register'),
                        'Métodos Permitidos': ['POST'],
                    },
                    'Perfil do Usuário': {
                        'Descrição': 'Obter informações do perfil do usuário',
                        'URL': reverse('user_profile'),
                        'Métodos Permitidos': ['GET'],
                    },
                    'Atualizar Perfil do Usuário': {
                        'Descrição': 'Atualizar informações do perfil do usuário',
                        'URL': reverse('user_profile_update'),
                        'Métodos Permitidos': ['PUT'],
                    },
                    'Login de Usuário': {
                        'Descrição': 'Fazer login e obter token de acesso',
                        'URL': reverse('token_obtain_pair'),
                        'Métodos Permitidos': ['POST'],
                    },
                    'Deletar Usuário': {
                        'Descrição': 'Excluir um usuário',
                        'URL': reverse('deleteUser', args=['1']),
                        'Métodos Permitidos': ['DELETE'],
                    },
                },
            },
            'Pedidos': {
                'Descrição': 'Gerenciar pedidos',
                'Endpoints': {
                    'Adicionar Itens ao Pedido': {
                        'Descrição': 'Adicionar itens a um novo pedido',
                        'URL': reverse('orders-add'),
                        'Métodos Permitidos': ['POST'],
                    },
                    'Meus Pedidos': {
                        'Descrição': 'Obter a lista de pedidos do usuário logado',
                        'URL': reverse('myorders'),
                        'Métodos Permitidos': ['GET'],
                    },
                    'Detalhes do Pedido': {
                        'Descrição': 'Obter detalhes de um pedido específico',
                        'URL': reverse('user-order', args=['1']),
                        'Métodos Permitidos': ['GET'],
                    },
                    'Pagar Pedido': {
                        'Descrição': 'Atualizar o status de pagamento de um pedido',
                        'URL': reverse('pay', args=['1']),
                        'Métodos Permitidos': ['PUT'],
                    },
                },
            },
            'Administração': {
                'Descrição': 'Painel de Administração do Django',
                'URL': reverse('admin:index'),
                'Métodos Permitidos': ['GET'],
            },
        }
    }

    formatted_api_info = json.dumps(api_info, indent=4, ensure_ascii=False)
    html_response = f'<pre>{formatted_api_info}</pre>'

    return HttpResponse(html_response)
