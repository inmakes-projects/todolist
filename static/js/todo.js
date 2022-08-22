const buttons = document.querySelectorAll('.btnDelete')
buttons.forEach( btn => {
    if (btn) {
        btn.addEventListener('click', (evt) => {
            if (confirm('Are you sure the item is completed?')) {
                btn.disabled = true;
                window.location.href = evt.target.dataset.href;
            }
        })   
    }
})

const deleteBtn = document.getElementById('btnDelete');
if (deleteBtn) {
    deleteBtn.addEventListener("click", (evt) => {
        if (confirm('Are you sure the item is completed?')) {
            document.getElementById('frmDeleteForm').submit();
        }
    });   
}