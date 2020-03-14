import { Injectable } from '@angular/core';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders, HttpRequest, HttpParams } from '@angular/common/http';


@Injectable()
export class AuthenticationService {
   // http options used for making API calls
  private httpOptions: any;

   // the actual JWT token
  public token: string;

   // the token expiration date
  public token_expires: Date;

   // the username of the logged in user
  public username: string;

   // error messages received from the login attempt
  public errors: any = [];

  constructor(private http: HttpClient) {
    this.httpOptions = {
      headers: new HttpHeaders({'Content-Type': 'application/json'})
    };
  }

    login(username: string, password: string, email:string) {
        console.log("user")
        return this.http.post<any>(`http://127.0.0.1:8000/login/`, { username: username, password: password,email: email})
            .pipe(map(user => {
              console.log("user token check",user)
                // login successful if there's a jwt token in the response
                if (user && user.token) {
                    console.log("token saved",user.token)

                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('token', user.token);

                    // console.log(localStorage.getItem('currentUser'))
                }
                else {console.log("user token not found")}

                return user;
            }));
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('token');
    }

    forgotuser(email:string) {
      return this.http.post<any>(`http://127.0.0.1:8000/forgotpassword/`, {email: email})
          .pipe(map(user => {
              // login successful if there's a jwt token in the response
              if (user && user.token) {
                  // store user details and jwt token in local storage to keep user logged in between page refreshes
                  localStorage.setItem('token', JSON.stringify(user));
              }

              return user;
          }));
    }

}
