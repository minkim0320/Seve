
    
    function clickTags(title, name) {
      console.log('in clickTags function');
      console.log(title);
      console.log(name);
      console.log('ending clickTags function');

      var x = document.getElementById('divone');
      var y = document.getElementById('divtwo');
      x.style.display = '';
      y.style.display = 'none';

      var title_id = document.getElementById('title');
      var contents_id = document.getElementById('testing');

      contents_id.readOnly = false;

      title_id.value = title;
      contents_id.innerHTML = name;
  }

  function displaySaved() {
      var x = document.getElementById('divone');
      var y = document.getElementById('divtwo');

      if( x.style.display == 'none'){
          console.log('here')
          x.style.display = '';
          y.style.display = 'none';
      } else if (x.style.display == '') {
          x.style.display = 'none';
          y.style.display = '';
      }

      var url = 'http://localhost:5000/notes';
      fetch(url).then(function (response) {
         return response.json(); 
      }).then(function(data) {

          var tempDiv = document.getElementById("divtwo");
          while(tempDiv.firstChild) {
              tempDiv.removeChild(tempDiv.firstChild);
          }

          var savedNotes = document.createElement('h3');
          savedNotes.innerHTML = 'Saved Notes';
          var element = document.getElementById("divtwo");
          element.appendChild(savedNotes);

          console.log(data);
          keys = Object.keys(data)

          for (var i = 0; i < Object.keys(data).length; i++){
              var tag2 = document.createElement('button');
              var text2 = document.createTextNode('Title: ' + data[keys[i]]['Title']);
              // tag2.href = "http://google.com";
              tag2.className = 'btn btn-secondary';
              tag2.setAttribute('onclick', 'clickTags(\`' + data[keys[i]]['Title'] + '\`, \`' + data[keys[i]]['Notes'] + '\`);');
              tag2.style='text-align:left; background-color:white; color: black; font-weight:bold; text-decoration: none;'
              tag2.appendChild(text2);
              var element = document.getElementById("divtwo");
              element.appendChild(tag2);

              var tag = document.createElement("p");
              var text = document.createTextNode('Notes: ' + data[keys[i]]['Notes']);
              tag.style='text-align:left; background-color:white;'
              tag.appendChild(text);
              element.appendChild(tag);
          }

      });

  }

  function PreviewImage() {
      var oFReader = new FileReader();
      oFReader.readAsDataURL(document.getElementById("image").files[0]);

      oFReader.onload = function (oFREvent) {
          document.getElementById("uploadPreview").src = oFREvent.target.result;
      };
  };

  function post_text() {
      var url = 'http://localhost:5000/test';
      var text = document.getElementById('testing').value
      var title = document.getElementById('title').value

      fetch(url, {
          method: "post",
          headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
          },

          //make sure to serialize your JSON body
          body: JSON.stringify({
              title: title,
              notes: text
          })
      })
      // .then( (response) => { 
      //     //do something awesome that makes the world a better place
      // });
  }

  function change_text() {
      var url = 'http://localhost:5000/home';
      fetch(url).then(function (response) {
         return response.json(); 
      }).then(function(data) {
          arr = data.text // ["Where it began..","Greece, 400 BC", "Credited for coining the term \"atom\"","divided anymore, hello"]
          console.log(arr);

          arrToString = '';
          for (var i = 0; i< arr.length; i++){
              arrToString += arr[i] + '\n';
          }

          var x = document.getElementById('testing');
          x.readOnly = false;

          if (x.innerHTML === '') {
              // Section
              // var answer = y.replace(new RegExp('\n', 'g'), '<br>');
              x.innerHTML = arrToString;
          } else {
              x.innerHTML = '';
          }

      });
      
  }