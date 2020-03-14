import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user.service';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-resetpassword',
  templateUrl: './resetpassword.component.html',
  styleUrls: ['./resetpassword.component.css'],
  providers: [UserService]
})
export class ResetpasswordComponent implements OnInit {
  reset;
  username:string;

  constructor(private userService : UserService,private dataRoute: ActivatedRoute) { }

  ngOnInit() {
    this.reset = {
      password: '',
    };
    this.username = this.dataRoute.snapshot.paramMap.get("name");
    console.log("username = ", this.dataRoute.snapshot.paramMap.get("name"))
  }
  resetuser() {

    this.userService.resetuser(this.reset,this.username).subscribe(
      response => {
        alert('Password has been Updated Successfully')
      },
      error => console.log('error',error)

    );

  }
}
