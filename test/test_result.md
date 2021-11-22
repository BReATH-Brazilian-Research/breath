# service_constructor

## Especificação

- Tipo: Classes de equivalência
- Operação: Inicializar serviços
- Parâmetros:
  
| Classe | Valor | Resultado |
| ------ | ------ | --|
| Serviço Válido | service_name = "BDAcessPoint" | Sem exceção
| Serviço Inválido | service_name = "random_wrong_service_name" | Exceção: ValueError

## Resultados

### Primeira iteração:
```
======================================================================
ERROR: test_creation_fail (service_creator.ProcessCreationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\eltsu\Documents\GitHub\breath-brazilian-research-of-atmosphere-towards-health\test\service_creator.py", line 14, in test_creation_fail
    session_manager.create_service("random_wrong_service_name")
  File "..\src\breath\session_manager\session_manager.py", line 19, in create_service
    request_queue, response_queue = self._service_constructor.create_service(service_name, self._queue, self._global_response_queue)
TypeError: cannot unpack non-iterable NoneType object

----------------------------------------------------------------------
Ran 2 tests in 0.008s
```
- Motivo: retorna da função em caso inválido incorreto -> Alterar o retorno

### Segunda iteração:
```
======================================================================
FAIL: test_creation_fail (service_creator.ProcessCreationTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\eltsu\Documents\GitHub\breath-brazilian-research-of-atmosphere-towards-health\test\service_creator.py", line 14, in test_creation_fail
    session_manager.create_service("random_wrong_service_name")
AssertionError: ValueError not raised

----------------------------------------------------------------------
Ran 2 tests in 0.008s

FAILED (failures=1)
```
  - Motivo: não está lançando a exceção no caso inválido

### Terceira iteração:

```
----------------------------------------------------------------------
Ran 2 tests in 0.008s

OK
```