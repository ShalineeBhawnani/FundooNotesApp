import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { map } from 'rxjs/operators';

@Injectable()
export class AuthenticationService {
    constructor(private http: HttpClient) { }

    login(username: string, password: string, email:string) {
        console.log("user")
        return this.http.post<any>(`http://127.0.0.1:8000/login/`, { username: username, password: password,email: email})
            .pipe(map(user => {
              console.log("user token check")
                // login successful if there's a jwt token in the response
                if (user && user.token) {
                    console.log("token saved",user.token)
                    // store user details and jwt token in local storage to keep user logged in between page refreshes
                    localStorage.setItem('currentUser', JSON.stringify(user));
                    console.log(localStorage.getItem('currentUser'))
                }
                else {console.log("user token not found")}

                return user;
            }));
    }

    logout() {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
    }
    forgotuser(email:string) {
      return this.http.post<any>(`http://127.0.0.1:8000/forgotpassword/`, {email: email})
          .pipe(map(user => {
              // login successful if there's a jwt token in the response
              if (user && user.token) {
                  // store user details and jwt token in local storage to keep user logged in between page refreshes
                  localStorage.setItem('currentUser', JSON.stringify(user));
              }

              return user;
          }));
    }

}
