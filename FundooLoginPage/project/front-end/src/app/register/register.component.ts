import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css'],
  providers: [UserService]
})
export class RegisterComponent implements OnInit {
  register;

  constructor(private userService : UserService) {}
  ngOnInit(){
    this.register = {
      name: '',
      username: '',
      email: '',
      password: '',
      password2: ''
    };
  }
  registerUser() {
    this.userService.registerUser(this.register).subscribe(
      response => {
        alert('User ' + this.register.username + 'please verify through your mail')
      },
      error => console.log('error',error)

    );

  }

}


