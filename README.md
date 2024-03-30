# ReGex 

Nesse repositório, abordaremos conceitos e usos do Regex. Meu objetivo é criar um material de estudos e introduzir pessoas ao assunto, fornecendo uma compreensão sobre expressões regulares e suas aplicações práticas.

Ao longo deste documento, utilizaremos exemplos de Regex na linguagem Python assim como as características da biblioteca `re`.

Recomendo que aplique os exemplos que temos nesse repositório e também faça seus testes, tenha um bom proveito!

## Sumário

- [ReGex](#regex)
  - [O que é? Para que serve?](#o-que-é-para-que-serve)
  - [Material de apoio](#material-de-apoio)
  - [Um .find() mais poderoso](#um-find-mais-poderoso)
  - [O uso da raw string `r""`](#o-uso-da-raw-string-r)
  - [Meta-caracteres](#meta-caracteres)
    - [Conjuntos](#conjuntos)
    - [Abreviações](#abreviações)
    - [Âncoras `^ $ \b`](#âncoras--b)
    - [Multiplicadores `{min,max} e *`](#multiplicadores-minmax-e-)
    - [Ou `|`](#ou-|)
    - [Multiplicador `+`](#multiplicador-)
  - [Lookahead e Lookbehind](#lookahead-e-lookbehind)
    - [Lookahead Positivo `(?=...)`](#lookahead-positivo-)
    - [Lookahead Negativo `(?!...)`](#lookahead-negativo-)
    - [Lookbehind Positivo `(?<=...)`](#lookbehind-positivo-)
    - [Lookbehind Negativo `(?<!...)`](#lookbehind-negativo-)
- [Aplicando no Python](#aplicando-no-python)
  - [Importando o ReGex](#importando-o-regex)
    - [Usando o `re.compile`](#usando-o-recompile)
  - [Match](#match)
    - [Fullmatch](#fullmatch)
    - [Search](#search)
    - [FindAll](#findall)
  - [Flags do re](#flags-do-re)
- [UTILS - Algumas Patterns utilitárias](#utils---algumas-patterns-utilitárias)

## O que é? Para que serve? 

O Regex, abreviação de _<u>Re</u>gular <u>Ex</u>presions_  é um tipo de formato para identificar termos que se repetem ou seguem algum padrão de caracteres, em um determinado texto.

Diversas linguagens de programação suportam o Regex, sendo uma forte ferramenta na área do desenvolvimento

Principais usos do ReGex:

- Validar padrões de caracteres;
- Verificar a existência de expressões em um texto;
- Extrair e tratar padrões;
- Substituir expressões por outras.

## Material de apoio

Nesta seção, você encontrará recursos para aprender e praticar expressões regulares.

#### Documentação oficial da biblioteca `re` do Python:

- [Docs regex python](https://docs.python.org/pt-br/3/library/re.html)

#### Repositórios usados como referência:

- [Regex by: EuCarlos](https://github.com/EuCarlos/RegEx?tab=readme-ov-file)

- [learn-regex by: ziishaned](https://github.com/ziishaned/learn-regex/blob/master/translations/README-pt_BR.md)

#### Sites para treinar regex:

- [regex101](https://regex101.com/)

- [regexone (Jogo 🎮)](https://regexone.com/)


## Um .find() mais poderoso

Pense no seguinte problema: Você recebeu um arquivo o qual contém várias informações, entre elas o peso em quilos de vários itens. Você tem interesse de extrair apenas o valor dos pesos, contudo eles variam podendo ter mais casas decimais ou menoos, além disso existe outro problema, algumas partes desse texto estão 'sujos', isto é, caracteres indesejados podem estar na mesma palavra. Seu objetivo agora é saber quando uma palavra desejada começa (Nesse caso o pesso em kg) e também os seus respectivos textos, sem outras palavras grudadas.

Para fazer esta tarefa você cria a seguinte função:

```python
# Alguns exemplos de casos:
case_1 = '1400kg'
case_2 = '20kg'
case_3 = 'ab500kg'
```

```python
def find_kg(string: str) -> list | None:
    kg_index = string.find('kg')
    if kg_index != -1:
        start_index = kg_index
        while start_index > 0 and string[start_index - 1].isdigit():
            start_index -= 1
        return [(start_index, kg_index + 2), string[start_index:kg_index + 2]]

find_kg(case_1)
```
saída:
```
[(0, 6), '1400kg']
```

Apesar dessa função não ser a mais elegante ou performática, perceba que em mesmo o exemplo mais simples, foi necessário usar métodos como o .find() assim como estruturas de repetição.

Agora veja o quão simplificado fica ao usar expressões regulares:

```python
import re

kg_pattern = r"\d*kg"

re.search(pattern=kg_pattern, string=case_1)
```

saída:
```
<re.Match object; span=(0, 6), match='1400kg'>
```

Perceba como ficou mais simples com a expressão regular, isso considerando um exemplo fácil, sem dúvidas o ReGex é uma ferramenta poderosa!

Mas algumas dúvidas surgem, afinal o que é `pattern` ? qual é o motivo de usar um `r` antes de uma string ? o que significa `\d*`? 

Não se preocupe, tudo será explicado ao decorrer do texto.

## O uso da raw string `r""`

Uma raw string em Python é uma forma de representar uma string de forma literal, sem interpretar caracteres de escape ou também conhecidos como _Escape Characters_, que são comumente os caracteres 'não vistos' e que representam algo dentro do texto, a seguir podemos ver uma tabela com alguns deles:


| Código | Resultado       |
|--------|-----------------|
| `\'`   | Aspas Simples   |
| `\\`   | Barra Invertida |
| `\n`   | Nova Linha      |
| `\t`   | Tab             |
| `\b`   | Backspace       |

Ou seja, ao indicar uma string com um r na frente: `r""` estamos dizendo ao python que vamos fazer o uso de raw strings, isto é, o código vai interpretar o texto de forma literal. É recomendado que ao fazer uso do Regex também se utilize das raw strings, visto que em certos casos eles evitam conflitos ou algumas confusões ao gerar nosso formato de pattern.

### O que é uma `Pattern`?

`Pattern` é um modelo que compõem meta-caracteres que regem "um padrão a ser seguido", eles tem suas próprias regras e condições para que ocorra um `match`, que é quando uma string corresponde (Retorna verdadeiro) para um modelo estabelecido.

Para aprender a estruturar uma pattern, primeiro precisamos entender alguns de seus comportamentos e também o uso dos Meta-caracteres, algo que será abordado a seguir

## Meta-caracteres

Meta-Caracteres no ReGex são caracteres que representam alguma regra ou condição composta ma pattern, por conta disso certos caracteres são reservados , então se quisermos representar eles no formato original, precisamos usar a barra `\` seguido do caractere, exemplo: o ponto `.` é reservado para qualquer caractere, mas se usarmos `\.` ele vai representar apenas um ponto "." na string 

A seguir podemos ver a tabela que demonstra o Meta-Caracter e sua descrição:

|Meta-Caracteres|Descrição|
|:----:|----|
|.|Corresponde a qualquer caractere, exceto uma quebra de linha|
|[ ]|Classe de caracteres. Corresponde a qualquer caractere contido dentro dos colchetes.|
|[^ ]|Classe de caracteres negada. Corresponde a qualquer caractere que não está contido dentro dos colchetes.|
|*|Corresponde a 0 ou mais repetições do símbolo anterior.|
|+|Corresponde a 1 ou mais repetições do símbolo anterior.|
|?|Faz com que o símbolo anterior seja opcional.|
|{n,m}|Chaves. Corresponde a no mínimo "n" mas não mais que "m" repetições do símbolo anterior.|
|(xyz)|Grupo de caracteres. Corresponde aos caracteres xyz nesta exata ordem.|
|&#124;|Alternância. Corresponde aos caracteres antes ou os caracteres depois do símbolo|
|&#92;|Escapa o próximo caractere. Isso permite você utilizar os caracteres reservados <code>[ ] ( ) { } . * + ? ^ $ \ &#124;</code>|
|^|Corresponde ao início da entrada.|
|$|Corresponde ao final da entrada.|

<small>by: ziishaned</small>


### Conjuntos `[ ]`

Os conjuntos [ ] em expressões regulares são utilizados para especificar um conjunto de caracteres possíveis em determinada posição na string. Por exemplo:

[aeiou] corresponde a qualquer vogal minúscula.
[A-Za-z] corresponde a qualquer letra maiúscula ou minúscula.
[0-9] corresponde a qualquer dígito de 0 a 9.
Além disso, podemos utilizar quantificadores dentro dos conjuntos, como +, *, {n,m}, para indicar repetições dos caracteres no conjunto.


### Abreviações

|Abreviação|Descrição|
|:----:|----|
|.|Qualquer caractere, exceto nova linha|
|\w|Corresponde a caracteres alfanuméricos: `[a-zA-Z0-9_]`|
|\W|Corresponde a caracteres não alfanuméricos: `[^\w]`|
|\d|Corresponde a dígitos: `[0-9]`|
|\D|Corresponde a não dígitos: `[^\d]`|
|\s|Corresponde a caracteres de espaços em branco: `[\t\n\f\r\p{Z}]`|
|\S|Corresponde a caracteres de espaços não em branco: `[^\s]`|

<small>by: ziishaned</small>

As abreviações são maneiras mais curtas de escrever um conjunto de certos caracteres, os conjuntos ou classes de caracteres são representados por colchetes, nessa caso vamos pegar o `\d` de exemplo, ele representa o dígitos de 0 até 9, ou seja, tudo que está de `[0-9]` ou até mesmo a versão estendida, que seria: `[0123456789]`.

Agora vamos pegar um """conjunto negação""" do `\d` o `\D` maiúsculo, que representa tudo aquilo que está fora de um conjunto de abreviação. Para representar um conjunto de classes negadas, isso é, tudo o que está fora do conjunto, utilizamos o sinal `^` dentro dos colchetes, veja o exemplo do `\D` = `[^\d]` ou `[^0123456789]`


**Dica:** Os meta-caracteres de abreviação que incluem um conjunto são os de barra letra minúscula, já suas negações são representadas por barra letra maiúscula.


### Âncoras `^ $ \b`

As âncoras `^`, `$` e `\b` têm funções específicas em expressões regulares:

- `^`: Especifica o início de uma linha.
  - Exemplo: `^python` corresponde a linhas que começam com "python".

- `$`: Especifica o fim de uma linha.
  - Exemplo: `python$` corresponde a linhas que terminam com "python".

- `\b`: Especifica uma fronteira de palavra (word boundary). Isso significa que `\b` corresponde a uma posição onde o caractere anterior é um caractere de palavra (como letras, dígitos ou underscore) e o próximo caractere não é um caractere de palavra, ou vice-versa.
  - Exemplo: `\bpython\b` corresponde a palavras completas "python" em um texto.

<small>O comando `\b` é extremamente útli, contudo ele não representa engloba os conjuntos dos caracteres especias, como `$ # @ ...`, uma das formas possíveis para contornar isso é utilizar a estrutura de lookhead: `(?!\s)text_here(?=\s|$)`</small>

### Multiplicadores `{min,max} e *`

Os multiplicadores {min,max} e * são usados para especificar a quantidade de repetições de um padrão na string.

{min,max}: Especifica que o padrão anterior deve ocorrer no mínimo "min" vezes e no máximo "max" vezes.

Exemplo: a{2,4} corresponde a "aa", "aaa" ou "aaaa".
*: Corresponde a 0 ou mais repetições do padrão anterior.

Exemplo: ba* corresponde a "b", "ba", "baa", "baaa", etc.
Esses multiplicadores ao encontrar repetições em um padrão da expressão regular.

### Ou `|`

O operador | (pipe) é utilizado para especificar alternativas em uma expressão regular. Ele funciona como uma operação de "ou", onde a expressão corresponde a qualquer uma das alternativas separadas pelo pipe.

Exemplo: gato|cachorro corresponde a "gato" ou "cachorro".
O uso do operador | é útil para criar expressões regulares mais flexíveis e abrangentes, permitindo combinar diferentes padrões em uma única expressão.


### Multiplicador `+`

O multiplicador `+` é usado para especificar que o padrão anterior deve ocorrer pelo menos uma vez, mas pode se repetir indefinidamente.

- Exemplo: `a+` corresponde a "a", "aa", "aaa", etc., mas não corresponde a uma string vazia.

Use para garantir que pelo menos uma repetição de um padrão ocorra na string.

## Quantificador `?`

O quantificador `?` é usado para especificar que o padrão anterior é opcional, ou seja, pode ocorrer zero ou uma vez na string.

- Exemplo: `colou?r` corresponde a "color" e "colour".

O quantificador `?` é útil para lidar com casos em que um caractere ou padrão pode estar presente ou não na string, tornando a expressão regular mais flexível e abrangente.



Claro, vou adicionar um capítulo para lookahead e lookbehind em expressões regulares.

## Lookahead e Lookbehind

Lookahead e lookbehind são uma estruturas que permitem fazer correspondências com base no contexto em que um padrão é encontrado, sem incluir esse contexto na correspondência final. Digamos que você quer pegar o valor de um câmbio de uma string "USD 000.00" mas não quer que o termo "USD" apareça, outro exemplo é de valores em unidades "00un." o qual você não deseja o termo "un."

### Lookahead Positivo `(?=...)`

O lookahead positivo é representado por `(?=...)` e é usado para fazer correspondência apenas se o padrão dentro do lookahead for encontrado à frente da posição atual na string, sem consumir caracteres na correspondência.

- Exemplo: `foo(?=bar)` corresponde a "foo" apenas se seguido por "bar", mas "bar" não é incluído na correspondência.

### Lookahead Negativo `(?!...)`

O lookahead negativo é representado por `(?!...)` e é usado para fazer correspondência apenas se o padrão dentro do lookahead não for encontrado à frente da posição atual na string, sem consumir caracteres na correspondência.

- Exemplo: `foo(?!bar)` corresponde a "foo" apenas se não seguido por "bar".

### Lookbehind Positivo `(?<=...)`

O lookbehind positivo é representado por `(?<=...)` e é usado para fazer correspondência apenas se o padrão dentro do lookbehind for encontrado atrás da posição atual na string, sem consumir caracteres na correspondência.

- Exemplo: `(?<=foo)bar` corresponde a "bar" apenas se precedido por "foo", mas "foo" não é incluído na correspondência.

### Lookbehind Negativo `(?<!...)`

O lookbehind negativo é representado por `(?<!...)` e é usado para fazer correspondência apenas se o padrão dentro do lookbehind não for encontrado atrás da posição atual na string, sem consumir caracteres na correspondência.

- Exemplo: `(?<!foo)bar` corresponde a "bar" apenas se não precedido por "foo".


# Aplicando no Python

Agora que vimos como compor uma `Pattern` está na hora de por em prática e aprender os principais métodos e funções no python


## Importando o ReGex

O Regex já é uma biblioteca padrão do python, não sendo necessário em casos comuns baixar ela pelo `pip`, para importar ela é muito simples, basta utilizar o seguinte comando:
```
import re
```

### Usando o `re.compile`

Para criar um tipo de pattern básica, podemos usar o `re.compile(<FormatHere>)`, ao criar esse objeto, nos poderemos utilizar e consumir ele na maioria das funções e métodos da bilioteca.

```python
pattern = re.compile(r"hello world")
```

## Match

É um método que localiza e retorna um objeto caso a pattern corresponda com a string utilizada. Caso contrário, retorna `None`

```
import re

pattern = r'hello'
string = 'hello world'

re.match(pattern, string)
```

Contido neste objeto podemos ver o `span=(n,n)` que informa os indices de inicio e fim desta string, já o `match='string here'` vai informar qual foi o match feito pela função

Para acessar os atributos desse objeto podemos usar os dois métodos:

```python
slice_string = catch.span()
text_finded =  catch.group()

print(f'Indices da string: {slice_string}')
print(f'Texto obtido: {text_finded}')
```

Saída:
```python
Indices da string: (0,5)
Texto obtido: hello
```

### Fullmatch

É semelhante ao Match, contudo só retorna um objeto se a string corresonder exatamente com a `Pattern`

```python

import re

string = "hello world"

pattern = re.compile(r"hello world")

catch = re.fullmatch(pattern, string)

print(catch)
```

Saída:
```python
<re.Match object; span=(0, 11), match='hello world'>

```

### Search

É o metodo que retorna sempre a primeira ocorrência que atende ao padrão da pattern

```python
import re

string = "Documento criado no dia 10/02/2022 documento revisado na data 12/06/2023"

pattern = re.compile(r"\d{2}[//]\d{2}[//]\d{4}")

search_catch = re.search(pattern, string)

print(search_catch)

```

Saída:
```python
<re.Match object; span=(24, 34), match='10/02/2022'>
```

### FindAll

O findAll localiza e nos retorna uma lista das palavras que corresponderam com nossa pattern

```python
import re

string = "Esses são os meus afazeres do dia a dia"

pattern_date = re.compile(r"dia")

all_matchs = re.findall(pattern_date, string)

print(all_matchs)
```

Saída
```python
['dia', 'dia']
```

Caso não obtenha nenhuma correspondência, será retornado uma lista vazia

```python
import re

string = "Esses são os meus afazeres do dia a dia"

pattern_date = re.compile(r"noite")

all_matchs = re.findall(pattern_date, string)

print(all_matchs)
```

Saída:
```python
[]
```
## Flags do re

Ao usar um método da biblioteca `re` podemos utilizar algumas `flags`, elas são parâmetros o qual mudam o comportamento do método, sendo úteis para determinados casos que precisamos configurar ou mudar o comportamento padrão das nossas operações de correspondência. 

A seguir, temos listado algumas das flags possíveis de utilizar da biblioteca

1. **re.IGNORECASE ou re.I**: Faz a correspondência de forma ignorando o case, isso é, desconsiderando se um caractere é maiúscula ou minúscula.

   Exemplo:
   ```python
   import re

   pattern = re.compile(r'hello', re.IGNORECASE)
   result = pattern.match('Hello World')
   print(result.group()) 
   ```
  
  Saída
   ```python
   Hello
   ```

2. **re.DOTALL ou re.S**: Faz o ponto (.) corresponder a qualquer caractere, incluindo novas linhas.

   Exemplo:
   ```python
   import re

   pattern = re.compile(r'.+', re.DOTALL)
   result = pattern.match('Hello\nWorld')
   print(result.group()) 
   ```

   Saída:
   ```python
   Hello\nWorld

   #OU

   Hello
   World
   ```

3. **re.MULTILINE ou re.M**: Faz com que os metacaracteres ^ e $ correspondam ao início e ao fim de cada linha, em vez do início e do fim da string completa.

   Exemplo:
   ```python
   import re

   pattern = re.compile(r'^\w+', re.MULTILINE)
   result = pattern.findall('Hello\nWorld')
   print(result) 
   ```

   Saída:
   ```
   ['Hello', 'World']
   ```

4. **re.VERBOSE ou re.X**: Permite que você escreva expressões regulares mais legíveis, ignorando espaços em branco e comentários, serve para explicar dentro do código o funcionamento da pattern.

   Exemplo:
   ```python
   import re

   pattern = re.compile(r'''
       \d{3}  # Três dígitos
       -      # Hífen
       \d{2}  # Dois dígitos
       -      # Hífen
       \d{4}  # Quatro dígitos
   ''', re.VERBOSE)

   result = pattern.match('123-45-6789')
   print(result.group())  
   ```
   Saída
   ```
   123-45-6789
   ```

5. **re.ASCII ou re.A**: Faz com que a classe de caracteres \w, \W, \b, \B, \d, \D, \s e \S correspondam apenas aos caracteres ASCII.

   Exemplo:
   ```python
   import re

   pattern = re.compile(r'\w+', re.ASCII)
   result = pattern.findall('Hello 你好')
   print(result)
   ```

   Saída:
   ```
   ['Hello']
   ```

6. **re.DEBUG**: É uma forma mais avançada para exibir informações de depuração sobre a expressão compilada

    Exemplo:
    ```
    import re

    # Expressão regular de exemplo para encontrar números de telefone no formato (XX) XXXX-XXXX
    pattern = re.compile(r'\(\d{2}\) \d{4}-\d{4}', re.DEBUG)
    # A expressão regular '\(\d{2}\) \d{4}-\d{4}' corresponde a números de telefone no formato (XX) XXXX-XXXX

    texto = "Entre em contato pelo telefone (12) 3456-7890 ou pelo celular."

    correspondencias = pattern.match(texto)

    print(correspondencias)
    ```

    Saída:
    ```
      LITERAL 40
    MAX_REPEAT 2 2
      IN
        CATEGORY CATEGORY_DIGIT
    LITERAL 41
    LITERAL 32
    MAX_REPEAT 4 4
      IN
        CATEGORY CATEGORY_DIGIT
    LITERAL 45
    MAX_REPEAT 4 4
      IN
        CATEGORY CATEGORY_DIGIT

    0. INFO 8 0b1 14 14 (to 9)
          prefix_skip 1
          prefix [0x28] ('(')
          overlap [0]
    9: LITERAL 0x28 ('(')
    11. REPEAT_ONE 9 2 2 (to 21)
    15.   IN 4 (to 20)
    17.     CATEGORY UNI_DIGIT
    19.     FAILURE
    20:   SUCCESS
    21: LITERAL 0x29 (')')
    23. LITERAL 0x20 (' ')
    25. REPEAT_ONE 9 4 4 (to 35)
    29.   IN 4 (to 34)
    31.     CATEGORY UNI_DIGIT
    33.     FAILURE
    34:   SUCCESS
    35: LITERAL 0x2d ('-')
    37. REPEAT_ONE 9 4 4 (to 47)
    41.   IN 4 (to 46)
    43.     CATEGORY UNI_DIGIT
    45.     FAILURE
    46:   SUCCESS
    47: SUCCESS
    None
    ```

# UTILS - Algumas Patterns utilitárias 

Esse capítulo é destinado para o compartilhamento de algumas patterns que podem ser utilitárias em seus projetos, lembrando que sempre existe uma forma diferente no regex para fazer suas correspondências;

<br>

**Nota!** Apesar das patterns encontrarem um formato possível, ainda é necessário validar a informação! Por exemplo: `000.000.000-00` é um cpf possível, mas sabemos que o valor dele não é válido, pois não existe um cpf desse jeito.

------

- Fronteira de palavras que aceita mais caracteres que o \b:
```
(?!\s)text_here(?=\s|$)
```

- Formato Email simples
```
(\w+@\w+\.com(\.[a-z]{2})?)
```

- Formato para telefone (Formato: (XX) XXXXX-XXXX)
```
\(\d{1,3}\) ?(\d{5}-\d{4})
```

- Formato para CPF (Com pontuação)
```
\d{3}\.\d{3}\.\d{3}-\d{2}
```

- Formato para CNPJ (Com pontuação)
```
\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}
```

- Formato potências de mil e duas casas decimais (padrão brasileiro xx.xxx,xx)
```
(?!\s)((\d{1,3}\.(?=\d{3}))*(\d{3},\d{2})|\d{1,3},\d{2})(?=\s|$)
```

- Formato potências de mil monetário:
```
(?!\s)R\$((\d{1,3}\.(?=\d{3}))*(\d{3},\d{2})|\d{1,3},\d{2})(?=\s|$)
```

Explicação do potências de mil:


```
(?!\s) #fronteira de inicio
(
  (\d{1,3}\.(?=\d{3}))*(\d{3},\d{2})   # padrão para os pontos usando lookahead assertion xxx.xxx,xx
  |                                   # OU
  \d{1,3},\d{2}                       # padrão simples de max: xxx,xx min: x,xx
  )                                   # Grupo para que OU funcione
(?=\s|$) # fronteira de fim
```

Detalhando a operação lookahead assertion:

```
(\d{1,3}\.(?=\d{3})) #grupo 1, responsável por sempre encontrar xxx.xxx N vezes
(\d{3},\d{2})        #grupo 2, responsável por xxx,xx
                     #Nota: o tamanho mínimo para este padrão aceitar é x.xxx,xx


(\d{1,3}\.(?=\d{3})) #Sempre olha o grupo que começa no ponto e anda até 3 vezes para esquerda, depois disso se repete
                     #Ex: xxx.| desde que atrás da | seja xxx
                     # xxx.|xxx => xxx.

```