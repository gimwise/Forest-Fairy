// get all the stars
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

// get the form, confirm-box and csrf token
const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const ratedForm = document.querySelector('.rated-form')
const ratedScoreObj = document.getElementById('rated-score')

const errorMessage = document.querySelector(".error_messages")

// checked 속성 추가해주는 함수
const handleStarSelect = (size) => {
    const children = form.children
    for (let i=0; i < children.length; i++) {
        if(i <= size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

// 이미 생성된 별점에 checked 속성 추가해주는 함수
const handleRatedStarSelect = (size) => {
    const children = ratedForm.children
    for (let i=0; i < children.length; i++) {
        if(i < size) {
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}

// 마우스 올리면 별 색 변화시키는 함수
const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            // one.classList.add('checked')
            // two.classList.remove('checked')
            // three.classList.remove('checked')
            // four.classList.remove('checked')
            // five.classList.remove('checked')
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }
        default: {
            handleStarSelect(0)
        }
    }

}

const getNumericValue = (stringValue) =>{
    let numericValue;
    if (stringValue === 'first') {
        numericValue = 1
    } 
    else if (stringValue === 'second') {
        numericValue = 2
    }
    else if (stringValue === 'third') {
        numericValue = 3
    }
    else if (stringValue === 'fourth') {
        numericValue = 4
    }
    else if (stringValue === 'fifth') {
        numericValue = 5
    }
    else {
        numericValue = 0
    }
    return numericValue
}

if(errorMessage != null){
    alert("이미 존재하는 화장실입니다.")
}

if (one) {
    const arr = [one, two, three, four, five]

    if(ratedForm){
        ratedScoreNum = parseInt(ratedScoreObj.textContent)
        handleRatedStarSelect(ratedScoreNum)
    }else{
        arr.forEach(item=> item.addEventListener('mouseover', (event)=>{
            handleSelect(event.target.id)
        }))
    
        arr.forEach(item=> item.addEventListener('click', (event)=>{
            // rated score not numeric
            const val = event.target.id
            // console.log(val)
            let isSubmit = false
            form.addEventListener('submit', e=>{
                e.preventDefault()
                if (isSubmit) {
                    return
                }
                isSubmit = true
                
                // toilet id
                const id = e.target.id
                // rated score numeric
                const val_num = getNumericValue(val)
                // alert(val_num)
                $.ajax({
                    type: 'POST',
                    url: `/${id}/`,
                    data: {
                        'csrfmiddlewaretoken': csrf[0].value,
                        'tid': id,
                        'score': val_num,
                    },
                    success: function(response){
                        confirmBox.innerHTML = `<h6>${response.score} / 5점. 리뷰가 성공적으로 등록되었습니다.</h6>`
                        window.location.href = `/${id}/`
                    },
                    error: function(error){
                        confirmBox.innerHTML = '<h6>다시 시도해주세요.</h6>'
                    }
                })
            })
        }))
    }
}