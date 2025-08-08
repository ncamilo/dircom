# 🔌 Dircom

**Dircom** é um utilitário de linha de comando leve, multiplataforma e escrito em Python, para listar portas seriais disponíveis no sistema — com destaque para portas USB. Ideal para desenvolvedores que trabalham com ESP32, Arduino, Raspberry Pi, sensores e outros dispositivos seriais.

---

## 🚀 Funcionalidades

- Lista todas as portas COM/seriais disponíveis
- Filtra somente portas conectadas via USB (`--usb-only`)
- Marcação clara de portas USB com tag `[USB]`
- Compatível com **Windows**, **Linux** e **macOS**
- Interface por linha de comando, fácil de usar
- Compilável em `.exe` para uso offline em Windows

---

## 💻 Uso

```bash
python dircom.py
```

### Opções:

| Parâmetro        | Descrição                                |
|------------------|--------------------------------------------|
| `-u`, `--usb-only` | Mostra apenas portas USB                  |
| `-v`, `--version`  | Mostra a versão atual do utilitário       |
| `-h`, `--help`     | Exibe ajuda e instruções de uso           |

### Exemplos:

```bash
python dircom.py --usb-only
python dircom.py -v
```

---

## 🔧 Instalação

**Requisitos:**

- Python 3.6 ou superior
- Biblioteca `pyserial`

### Instale com pip:

```bash
pip install pyserial
```

---

## 🛠️ Compilando para `.exe` no Windows

Para distribuir como um executável standalone (sem Python instalado):

### 1. Instale o PyInstaller

```bash
pip install pyinstaller
```

### 2. Compile o script

```bash
pyinstaller --onefile --name dircom dircom.py
```

O executável será gerado em:

```
dist/dircom.exe
```

---

## 🐧 Linux/macOS

Você pode rodar com:

```bash
python3 dircom.py
```

Ou compilar com PyInstaller no próprio sistema operacional.

---

## 📂 Estrutura recomendada

```
dircom/
├── dircom.py
├── README.md
├── .gitignore
├── requirements.txt
└── LICENSE
```

---

## 📦 Requisitos

Conteúdo de `requirements.txt`:

```
pyserial>=3.5
```

---

## 📜 Licença

Distribuído sob a licença [MIT](LICENSE).

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests com melhorias, sugestões ou correções.

---

## 📝 TODO

- [x] Testar funcionalidade completa no **Windows**
- [ ] Testar no **Linux** com diversas distribuições
- [ ] Testar no **macOS** (ainda não verificado)
- [ ] Adicionar testes automatizados (opcional)
- [ ] Criar executável para Linux e macOS com PyInstaller
- [ ] Publicar no PyPI (como pacote Python)

---

Sinta-se à vontade para contribuir com testes ou melhorias!

## 🔗 Autor

**Nelson Almeida**  
[github.com/ncamilo](https://github.com/ncamilo)
