$(document).ready(function () {


  // code for select dropdown with image and select+++++++++++++++++++++++++++
  //test for getting url value from attr
  // var img1 = $('.test').attr("data-thumbnail");
  // console.log(img1);

  //test for iterating over child elements
  var langArray = [];
  $('.vodiapicker1 option').each(function () {

    var img = $(this).attr("data-thumbnail");
    var text = this.innerText;
    var value = $(this).val();
    var item = '<li class="' + value + '"><img src="' + img + '" alt="" value="' + value + '"/><span>' + text + '</span></li>';
    langArray.push(item);
    $(this).parents('.form-group').find('#myselect-inner').html(langArray);
    $(this).parents('.form-group').find('.btn-select').html($(this).parents('.vodiapicker').find('option').first().text());
  })
  var langArray2 = [];
  $('.vodiapicker2 option').each(function () {

    var img = $(this).attr("data-thumbnail");
    var text = this.innerText;
    var value = $(this).val();
    var item = '<li class="' + value + '"><img src="' + img + '" alt="" value="' + value + '"/><span>' + text + '</span></li>';
    langArray2.push(item);
    $(this).parents('.form-group').find('#myselect-inner').html(langArray2);
    $(this).parents('.form-group').find('.btn-select').html($(this).parents('.vodiapicker').find('option').first().text());
  })
  var langArray3 = [];
  $('.vodiapicker3 option').each(function () {

    var img = $(this).attr("data-thumbnail");
    var text = this.innerText;
    var value = $(this).val();
    var item = '<li class="' + value + '"><img src="' + img + '" alt="" value="' + value + '"/><span>' + text + '</span></li>';
    langArray3.push(item);
    $(this).parents('.form-group').find('#myselect-inner').html(langArray3);
    $(this).parents('.form-group').find('.btn-select').html($(this).parents('.vodiapicker').find('option').first().text());
  })
  var langArray4 = [];
  $('.vodiapicker4 option').each(function () {

    var img = $(this).attr("data-thumbnail");
    var text = this.innerText;
    var value = $(this).val();
    var item = '<li class="' + value + '"><img src="' + img + '" alt="" value="' + value + '"/><span>' + text + '</span></li>';
    langArray4.push(item);
    $(this).parents('.form-group').find('#myselect-inner').html(langArray4);
    $(this).parents('.form-group').find('.btn-select').html($(this).parents('.vodiapicker').find('option').first().text());
  })



  //Set the button value to the first el of the array

  // $('.btn-select').attr('value', 'en');

  //change button stuff on click
  $('#myselect-inner li').click(function () {
    $(this).parents('.myselect-wrap').siblings('.btn-select').html($(this).find('span').text());
    // $(this).parents('.myselect-wrap').siblings('.btn-select').attr('value', value);
    $(this).parents('.myselect-wrap').toggle();
    //console.log(value);
  });

  $(".btn-select").click(function () {
    $(this).siblings('.myselect-wrap').toggle();
    $(this).parents('.col-sm-12').siblings().find('.myselect-wrap').slideUp();
  });





  //check local storage for the lang
  var sessionLang = localStorage.getItem('lang');
  if (sessionLang) {
    //find an item with value of sessionLang
    var langIndex = langArray.indexOf(sessionLang);
    $('.btn-select').html(langArray[langIndex]);
    $('.btn-select').attr('value', sessionLang);
  } else {
    var langIndex = langArray.indexOf('ch');
    $('.btn-select').html(langArray[langIndex]);
    $('.btn-select').attr('value', 'en');
  }

  // code for select dropdown with image and select end+++++++++++++++++++++++



  // pop on btn click




  // $(".go").click(function () {
  //   categories = $('input[name="categories"]:checked').val();
  //   console.log(categories)
  //   if (categories == '' || categories == undefined) {
  //       $('.modal-wrapper').show();
  //       $("#modalMsg").text("Please Select Category.")
  //       return false
  //   }

  //   if (categories != 'None' && categories == 'co-branded-distributor') {
  //       $('.modal-wrapper').show();
  //       $("#modalMsg").text("To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.")


  //   return false
  //   } else if($('.lang-select button span').text() == 'Select Collateral Type*'){
  //     $('.modal-wrapper').show();
  //     $("#modalMsg").text("Please Select Category.")
  //     return false
  //   }else{
  //     $("#getForm").submit()
  //   }
  // });

  // $(".close-btn").click(function () {
  //   $('.modal-wrapper').fadeOut(350);
  // })

  $('.go-drop').click(function () {
    var msg = $(this).val();
    console.log(msg);
    $("#modalMsg").text("To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.")
    return false
  });

  $('#myselect-inner li.getpop').click(function () {
    $('.modal-wrapper').show();
    $("#modalMsg").text("To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.")
    return false
  });

  $('.single-slider-bottom .nxt-page , .error-list-bottom .next').click(function () {
    $('.page-slider .slick-current').next().find('.img-wrap').click();
    $('.slick-next ').click();
  });
  $('.single-slider-bottom .pre-page , .error-list-bottom .prev').click(function () {
    $('.page-slider .slick-current').prev().find('.img-wrap').click();
    $('.slick-prev').click();
  });


  $(".brand-check-title").on("click", function () {
    $(".observation-type").addClass("button-show");
    $(".display-msg").addClass("button-show");
  });
  $(".brand-summary-title").on("click", function () {
    $(".observation-type").removeClass("button-show");
    $(".display-msg").removeClass("button-show");
  });






  // aj  script starts here 
  const optionz = document.querySelectorAll('.optionz');
  const optionList = document.querySelectorAll('.optionList');
  const vlaue = document.querySelectorAll('.value');
  const listItem = document.querySelectorAll('.list-item');
  const submitBtn = document.getElementById('submitBtn');
  const modalWrapper = document.querySelector('.modal-wrapper');
  const modalMsg = document.getElementById('modalMsg');
  const closeBtn = document.querySelector('.close-btn')
  // variables 
  let formVal = [];
  let formFlag = true
  let flasValue = true;

  optionz.forEach((item, index) => {
    item.addEventListener('click', (e) => {
      optionList.forEach((it, id) => {
        if (index === id) {
          it.classList.toggle('hide');
          const liItem = it.children
          Array.from(liItem).forEach(function (element, eindex) {
            element.addEventListener('click', (e) => {
              const text = element.dataset.val;
              const coll_id = element.dataset.id;
              const coll_media = element.dataset.media;
              var textVal = ''
              $('#' + coll_media).attr('collateral-id', "")
              if (coll_id != '') {
                $('#' + coll_media).attr('collateral-id', coll_id)
              }

              if (element.classList.contains('disabled')) {
                modalMsg.innerText = 'To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.'
                modalWrapper.classList.add('active');
                formFlag = !formFlag
              }
              // set selected value
              item.innerText = text
              // formVal = text;
              it.classList.add('hide');
              // assign selected value
              formVal = $.unique(formVal);
              if (index === 0 && eindex != 0) {
                textVal = '1'
                formVal.push(textVal)
              } else if (index === 1 && eindex != 0) {
                textVal = '2'
                formVal.push(textVal)
              } else if (index === 2 && eindex != 0) {
                textVal = '3'
                formVal.push(textVal)
              } else if (index === 3 && eindex != 0) {
                textVal = '4'
                formVal.push(textVal)
              } else {
                formVal = jQuery.grep(formVal, function (value) {
                  return value != textVal;
                });
              }
              formVal = $.unique(formVal);


            })
          });
        } else {
          it.classList.add('hide')
        }
      })
    })
  })
  const inp = document.querySelectorAll('input');
  // function getcheckedValue(){
  //   let checkedValue;
  //   for(let i = 0; i < inp.length; i++){
  //     if(inp[i].type === 'radio' && inp[i].checked){
  //       checkedValue = inp[i].value
  //     }else{
  //       checkedValue
  //     }
  //   }
  //   formVal.push(checkedValue)
  // }
  $("#submitBtn").click(function (e) {
    e.preventDefault()
    var nwformVal = formVal.filter(function (elem, index, self) {
      return index === self.indexOf(elem);
    });
    console.log(nwformVal, nwformVal.length)

    if (nwformVal.length == 0) {
      formFlag = !formFlag
      modalMsg.innerText = 'Please select one category of your collateral'
      modalWrapper.classList.add('active')
    } else if (nwformVal.length > 1) {
      formFlag = !formFlag
      modalMsg.innerText = 'Please select only one category of your collateral'
      modalWrapper.classList.add('active')
    } else {

      var category = $("input[name=categories]:checked").val();

      if (category != '' && typeof (category) != 'undefined' && category != 'co-branded-distributor') {
        var coll_id = $('#print').attr('collateral-id')
        if (coll_id == '' || typeof (coll_id) == 'undefined') {
          var coll_id = $('#digital').attr('collateral-id')
          if (coll_id == '' || typeof (coll_id) == 'undefined') {
            var coll_id = $('#presentation').attr('collateral-id')
          }
        }
        if (coll_id != '' && typeof (coll_id) != 'undefined') {
          window.location = 'upload_pdf/' + coll_id
        }
      } else {
        formFlag = !formFlag

        if (category == 'co-branded-distributor') {
          modalMsg.innerText = 'To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.'

        } else {
          modalMsg.innerText = 'Please select category'
        }
        modalWrapper.classList.add('active')

      }

    }
  });

  // $("#cobranded").click(function (e) {
  //   modalMsg.innerText = 'To process this collateral for brand check manually, kindly forward a request to brandteam@abbott.com.'
  //   modalWrapper.classList.add('active');
  //   formFlag = !formFlag
  // })

  // $(closeBtn).click(function (e) {
  //   modalWrapper.classList.remove('active');
  //   if (!formFlag) {
  //     location.reload()
  //   }
  // })


  closeBtn.addEventListener('click', () => {
    modalWrapper.classList.remove('active');
    if (!formFlag) {
      location.reload()
    }
  })


  // SET BLNCK COLLATERAL ID ON DEFAULT SELECTION OF MEDIA
  $("#default-Print").click(function () {
    $('#print').attr('collateral-id', '')
    formVal = jQuery.grep(formVal, function (value) {
      return value != '1';
    });
  })
  $("#default-Digital").click(function () {
    $('#digital').attr('collateral-id', '')
    formVal = jQuery.grep(formVal, function (value) {
      return value != '2';
    });
  })

  $("#default-Video").click(function () {
    $('#video').attr('collateral-id', '')
    formVal = jQuery.grep(formVal, function (value) {
      return value != '3';
    });
  })

  $("#default-Presentation").click(function () {
    $('#presentation').attr('collateral-id', '')
    formVal = jQuery.grep(formVal, function (value) {
      return value != '4';
    });
  })

})