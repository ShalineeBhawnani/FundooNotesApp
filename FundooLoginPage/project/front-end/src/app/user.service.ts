import { Injectable } from '@angular/core';
import { HttpClient,HttpResponse,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';



@Injectable()
export class UserService {

  baseurl = "http://127.0.0.1:8000";
  // httpHeaders = new HttpHeaders({'Content-Type': 'application/json'});


  constructor(private http: HttpClient) { }

  login(userData): Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/login/',userData,{
      responseType: 'text',
    });

  }

  register(userData): Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/registration/',userData,{
      responseType: 'text',
    });

  }

//   register(user: User) {
//     return this.http.post(`${config.apiUrl}/users/register`, user);
// }

  forgotuser(userData): Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/forgotpassword/',userData,{
      responseType: 'text',
    });

  }

  resetuser(userData,username): Observable<any>

  {
    return this.http.post('http://127.0.0.1:8000/resetpassword/'+username,userData,{
      responseType: 'text',
    });

  }
  note(userData):Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/note/',userData,{
      responseType: 'text',

    });

  }

  label(userData):Observable<any>
{

      console.log(localStorage.getItem('token'))
      return this.http.post('http://127.0.0.1:8000/label/', userData, { headers: {
        'token': localStorage.getItem('token')
      } });
    }


  //   return this.http.post('http://127.0.0.1:8000/label/',userData,{ headers: httpOptions }
  //    );
  // }

//   label(userData): Observable<any> {
//     const body = {label: userData.label };
//     return this.http.post(this.baseurl + '/label/', body,
//     {headers: this.httpOptions};
//   }

// }
  }
