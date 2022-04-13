import tkinter as tk
from tkintertable import TableCanvas, TableModel
from tkintertable.Tables import TableCanvas
from tkintertable.TableModels import TableModel

model = TableModel()
table = TableCanvas(frame, model=model)