import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { UserService } from '../../services/user.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AuthenticationService } from '../../services/authentication.service';

import { AlertService } from '../../services/alert.service';
@Component({
  selector: 'app-forgotpassword',
  templateUrl: './forgotpassword.component.html',
  styleUrls: ['./forgotpassword.component.css'],
  providers: [UserService]
})
export class ForgotpasswordComponent implements OnInit {
  loginForm: FormGroup;
  loading = false;
  submitted = false;
  returnUrl: string;

  // forgot;

  constructor( private userService : UserService, private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private router: Router,
    private authenticationService: AuthenticationService,
    private alertService: AlertService) {}

  ngOnInit() {

    this.loginForm = this.formBuilder.group({
      email: ['', Validators.required],
    });
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  get f() { return this.loginForm.controls; }
  onSubmit() {
    this.submitted = true;
    if (this.loginForm.invalid)
    {
      return;
    }
    this.loading = true;
    this.authenticationService.forgotuser(this.f.email.value)
      .pipe(first())
      .subscribe(
          data => {
              this.router.navigate([this.returnUrl]);
          },
          error => {
              this.alertService.error(error);
              this.loading = false;
          });
        }
      }

//     this.userService.forgotuser(this.loginForm).pipe(first()).subscribe(
//       response => {
//         alert('Kindly click on the activation link which has sent to your registered email id')
//       },
//       error => console.log('error',error)

//     );

//   }

//



