function renameHabit(id) {
    console.log("Rename clicked:", id);
    const span = document.getElementById(`${id}`);
    const currentName = span.textContent;
    console.log("the id is ", id);
    span.innerHTML = `
        <form action="/rename" method="post">
            <input type="hidden" name="habit_id" value="${id}">
            <input type="text" name="new_name" value="${currentName}">
            <button class="button btn" type="submit">Save</button>
        </form>
    `
}
