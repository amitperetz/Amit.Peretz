fetch('https://reqres.in/api/users?page=2').then(
    response => response.json()
).then(
    responseJSON => createUserList(responseJSON.data)
)
    .catch(
        err =>console.log(err)
    );


function createUserList(users){
    console.log(users);
    const cMain = document.querySelector("main");
    for(let user of users){
       const section= document.createElement('section') ;
       section.innerHTML = `
           <img src ="${user.avatar}" alt="Pofile Pic"/>
           <div>
             ${user.first_name} ${user.last_name}
              <br>
              <a href="mailto:${user.email}">Send email</a>
           </div> ` ;
        cMain.appendChild(section);
    }
}


