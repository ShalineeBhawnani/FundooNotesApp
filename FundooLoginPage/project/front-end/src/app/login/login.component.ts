import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
  providers: [UserService]
})
export class LoginComponent implements OnInit {
  login;

  constructor(private Auth: UserService,
              private router: Router) { }

    ngOnInit(){
      this.login = {
        username: '',
        email: '',
        password: ''
      };
    }
    loginUser() {
      this.Auth.loginUser(this.login).subscribe(
        response => {
          // alert('User ' + this.login.username + 'Succesfully loggedin')
          this.router.navigate(['/nav'])
        },
        error => console.log('error',error)

      );

    }

  }


