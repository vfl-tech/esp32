# Exibindo Dígitos em um Display de 7 Segmentos com ESP32

Este projeto demonstra como exibir dígitos de 0 a 9 em um display de 7 segmentos usando o microcontrolador ESP32. O código controla cada segmento do display para representar diferentes dígitos.

## Requisitos de Hardware

- Placa de Desenvolvimento ESP32
- Display de 7 segmentos (ânodo comum ou cátodo comum)
- Resistores (valor apropriado para seu display)
- Cabos jumper
- Protoboard

## Conexões dos Pinos

Conecte os segmentos do display de 7 segmentos aos pinos GPIO especificados do ESP32:

| Segmento | Pino GPIO |
|----------|-----------|
| a        | 2         |
| b        | 4         |
| c        | 18        |
| d        | 19        |
| e        | 21        |
| f        | 22        |
| g        | 23        |

## Requisitos de Software

- Firmware MicroPython instalado no ESP32
- Thonny IDE ou qualquer outro IDE compatível com MicroPython

## Explicação do Código

### Importar Bibliotecas

```python
from machine import Pin
from time import sleep
```

- `machine.Pin` é usado para controlar os pinos GPIO do ESP32.
- `time.sleep` é usado para criar um atraso entre a exibição dos dígitos.

### Definir Pinos dos Segmentos

```python
segments = {
    'a': Pin(2, Pin.OUT),
    'b': Pin(4, Pin.OUT),
    'c': Pin(18, Pin.OUT),
    'd': Pin(19, Pin.OUT),
    'e': Pin(21, Pin.OUT),
    'f': Pin(22, Pin.OUT),
    'g': Pin(23, Pin.OUT),
}
```

- Um dicionário `segments` mapeia cada segmento do display de 7 segmentos para um pino GPIO específico no ESP32.

### Definir Dígitos

```python
digits = {
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'd', 'e', 'g'],
    '3': ['a', 'b', 'c', 'd', 'g'],
    '4': ['b', 'c', 'f', 'g'],
    '5': ['a', 'c', 'd', 'f', 'g'],
    '6': ['a', 'c', 'd', 'e', 'f', 'g'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}
```

- Um dicionário `digits` mapeia cada dígito (0-9) para os segmentos correspondentes que devem ser acesos para exibir o dígito.

### Função para Exibir Dígitos

```python
def display_digit(digit):
    for segment in segments.values():
        segment.value(0)
    for segment in digits[digit]:
        segments[segment].value(1)
```

- A função `display_digit` apaga todos os segmentos e, em seguida, acende os segmentos necessários para exibir o dígito desejado.

### Loop Principal

```python
while True:
    for digit in '0123456789':
        display_digit(digit)
        sleep(1)
```

- O loop principal exibe os dígitos de 0 a 9, um por um, com um atraso de 1 segundo entre cada dígito.

## Como Usar

1. Carregue o código no ESP32 usando o Thonny IDE ou outro IDE compatível com MicroPython.
2. Conecte o display de 7 segmentos aos pinos GPIO conforme a tabela de conexões.
3. Execute o código. O display de 7 segmentos começará a exibir os dígitos de 0 a 9 em loop.

Este projeto é uma excelente introdução para controlar displays de 7 segmentos com o ESP32 usando MicroPython.
