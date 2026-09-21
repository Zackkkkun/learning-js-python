let tasks = [];

function addTask(title){
    let task = {title, done:false};//js object, key-value pairs, could also be title:title
    tasks.push(task);
}

addTask("learn arrays or list");
addTask("learn functions");
addTask("learn objects");

console.log(tasks);