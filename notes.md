## 🧠 What is .venv

.venv = Virtual Environment

In simple terms:
A private Python universe for ONE project.
- It’s a self-contained folder that holds:
- its own python.exe
- its own pip
- its own installed libraries (like black, numpy, etc.)

![.venv analogy](<notes img/image.png>)

You NEVER edit anything inside .venv manually.

It’s managed by Python tooling.

```python 
python -m venv .venv
pip install -r requirements.txt
```
That's how real projects scale.

