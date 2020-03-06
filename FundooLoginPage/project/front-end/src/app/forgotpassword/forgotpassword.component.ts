import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';

@Component({
  selector: 'app-forgotpassword',
  templateUrl: './forgotpassword.component.html',
  styleUrls: ['./forgotpassword.component.css'],
  providers: [UserService]
})
export class ForgotpasswordComponent implements OnInit {
  forgot;

  constructor( private userService : UserService) { }

  ngOnInit() {
    this.forgot = {
      email: '',
    };
  }
  forgotuser() {
    this.userService.forgotuser(this.forgot).subscribe(
      response => {
        alert('Kindly click on the activation link which has sent to your registered email id')
      },
      error => console.log('error',error)

    );

  }

}

