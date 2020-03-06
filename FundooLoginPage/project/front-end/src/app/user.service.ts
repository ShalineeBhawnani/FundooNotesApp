import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class UserService {

  constructor(private http: HttpClient) { }

  loginUser(userData): Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/login/',userData,{
      responseType: 'text',
    });

  }

  registerUser(userData): Observable<any>
  {
    return this.http.post('http://127.0.0.1:8000/registration/',userData,{
      responseType: 'text',
    });

  }

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



}

