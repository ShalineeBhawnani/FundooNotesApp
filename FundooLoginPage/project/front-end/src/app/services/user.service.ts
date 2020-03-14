import { Injectable } from '@angular/core';
import { HttpClient,HttpResponse,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '../../environments/environment';



@Injectable()
export class UserService {

  baseUrl = environment.baseUrl;
  constructor(private http: HttpClient) { }

  login(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/login/',userData,{
      responseType: 'text',
    });

  }

  register(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/registration/',userData,{
      responseType: 'text',
    });

  }

  forgotuser(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/forgotpassword/',userData,{
      responseType: 'text',
    });

  }

  resetuser(userData,username): Observable<any>

  {
    return this.http.post(this.baseUrl+'/resetpassword/'+username,userData,{
      responseType: 'text',
    });

  }
  note(userData):Observable<any>
  {
    return this.http.post(this.baseUrl+'/note/',userData,{
      responseType: 'text',

    });

  }

  label(userData):Observable<any>
{

      console.log(localStorage.getItem('token'))
      return this.http.post(this.baseUrl+'/label/', userData, { headers: {
        'token': localStorage.getItem('token')
      } });
    }
  }
