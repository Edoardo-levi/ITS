const API_URL = "http://localhost:3000/tasks"



export const fetchTasks = async () => {
    const response = await fetch(API_URL)
    if (!response.ok) throw new Error("Errore Fetch")

    const data = await response.json();
    return data;
};


export const createTasks = async (text) => {
     await fetch(API_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text, completed: false })
    })
   
}


export const cancellaTask = async( id) =>{
    await fetch(API_URL + "/" + id, { method: "DELETE" });

}

export const ToggleTasks = async(id, completed) =>{
    await fetch(API_URL + "/" + id,
                {
                    method: "PATCH",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ completed: !completed })
                });
}