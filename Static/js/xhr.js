const postBtn = document.getElementById('ci-button');
// const getBtn = document.getElementById('ci-button');

const sendHttpRequest = (method,url,data) => {
    const promise = new Promise((resolve,reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open(method,url);
        xhr.setRequestHeader('Content-Type','application/json');
        xhr.onload = () =>{
            if (xhr.status==201){
                resolve(JSON.parse(xhr.response))
            }
            else{
                reject(xhr.response)
            }
        }
        xhr.send(JSON.stringify(data));
    });
    return promise;
}

const sendData = () => {
    sendHttpRequest('POST','https://hkrsinvgen.herokuapp.com/api/post/',{
        Billing_name : document.querySelector("#cn").value,
        Billing_Address : document.querySelector("#ca").value,
        Plan_Description : document.querySelector("#pd").value,
        Plan_Cost : document.querySelector("#pc").value,
        Quantity : document.querySelector('#q').value,
        Invoice_date : document.querySelector("#ind").value,
        Due_date: document.querySelector("#dd").value,
        Payment_mode : document.querySelector("#pm").value,
        Paid_date : document.querySelector("#pda").value,
        Paid_amt : document.querySelector("#pa").value,
        Mobile_number : document.querySelector("#bm").value,
    })
    .then(responseData => { 
        console.log(responseData);
    })
    .catch(err =>{
        console.log(err);
    })
    ;
};

// const getData = () => {
//     sendHttpRequest('GET','https://admin.aizotec.com/api/v1/version/').then(responseData => {
//         console.log(responseData)
//         for(obj_data in responseData){
//             console.log(responseData[obj_data].id ,responseData[obj_data].Version_no)
//         }
//     })
    
// };

postBtn.addEventListener('click',sendData)
// getBtn.addEventListener('click',getData)