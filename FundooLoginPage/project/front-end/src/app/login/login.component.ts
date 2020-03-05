import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [AuthService]
})
export class LoginComponent implements OnInit {
  login;

  constructor(private Auth: AuthService,
              private router: Router) { }

    ngOnInit(){
      this.login = {
        fullname: '',
        username: '',
        email: ''
      };
    }
    loginUser() {
      this.Auth.loginUser(this.login).subscribe(
        response => {
          alert('User ' + this.login.username + 'Succesfully loggedin')
        },
        error => console.log('error',error)

      );

    }

  }


