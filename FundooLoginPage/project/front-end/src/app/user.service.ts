import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class UserService {

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
    return this.http.post('http://127.0.0.1:8000/label/',userData,{
      responseType: 'text',

    });

}
}

