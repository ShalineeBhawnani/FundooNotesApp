import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { HttpClient, HttpResponse ,HttpHeaders} from '@angular/common/http';


@Component({
  // selector: 'app-label',
  templateUrl: './label.component.html',
  styleUrls: ['./label.component.css'],
  providers:[AuthenticationService],

})
export class LabelComponent implements OnInit {
   registerForm: FormGroup;
   loading = false;
   submitted = false;
  //  user_id = localStorage.getItem('token');


    constructor(
        private formBuilder: FormBuilder,
        private router: Router,
        private userService: UserService,
        private alertService: AlertService) { }

    ngOnInit() {

        this.registerForm = this.formBuilder.group({

            label: [''],

        });
    }

    // convenience getter for easy access to form fields
    get f() { return this.registerForm.controls; }

    onSubmit() {
        this.submitted = true;
        // let user_id=JSON.parse(localStorage.getItem('user'));

        // stop here if form is invalid
        if (this.registerForm.invalid) {
            return;
        }
        let labelData = {

          // user : this.user_id,


          label: this.registerForm.value

        }

          console.log("user details:",labelData)
          console.log("req body: ", this.registerForm.value);

        this.loading = true;
        this.userService.label(labelData)
            .subscribe(
                data => {
                    this.alertService.success('label created successfully', true);
                    this.router.navigate(['/nav']);
                },
                error => {
                    this.alertService.error(error);
                    this.loading = false;
                });
    }
}
