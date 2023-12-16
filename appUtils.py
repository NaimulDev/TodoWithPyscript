from pyscript import document

def createTodoElement(todoTxt:str):
    deleteBtn = document.createElement("button")
    label = document.createElement("label")
    label.innerText = todoTxt
    deleteBtn.innerText = "x"
    deleteBtn.style.marginLeft = "1em"
    deleteBtn.style.marginBottom = "0.5em"
    deleteBtn.classList.add("btn")
    deleteBtn.classList.add("btn-danger")
    deleteBtn.style.padding = "5px"
    deleteBtn.style.backgroundColor = "#ff7fb0"
    deleteBtn.style.borderRadius = "50%"

    todoRowEl = document.createElement("tr")
    todoLabelCell = document.createElement("td")
    todoDelBtnCell = document.createElement("td")
    todoLabelCell.appendChild(label)
    todoDelBtnCell.appendChild(deleteBtn)
    todoRowEl.appendChild(todoLabelCell)
    todoRowEl.appendChild(todoDelBtnCell)

    todoRowEl.style.backgroundColor = "#ffc7c8"
    todoRowEl.style.padding = "5px"
    todoRowEl.style.border = "2px solid #fff"
    todoRowEl.style.boxShadow = "0 20px 50px rgba(240, 46, 170, 0.7)"
    todoRowEl.style.borderRadius = "10px"


    def del_task(evt):
        print("Deleting task...")
        rowEl = evt.target.parentNode.parentNode
        tableEl = rowEl.parentNode
        tableEl.removeChild(rowEl)
    
    deleteBtn.onclick = del_task
    
    return todoRowEl