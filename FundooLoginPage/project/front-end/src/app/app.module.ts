import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';
import { HttpClientModule ,HTTP_INTERCEPTORS} from '@angular/common/http';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { UserService } from './services/user.service';
import { AlertService } from './services/alert.service';
import { AuthGuard } from './auth_guard/auth.guard';
import { RegisterComponent } from './components/register/register.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppMaterialModule } from './app-material/app-material.module';
import { ForgotpasswordComponent } from './components/forgotpassword/forgotpassword.component';
import { ResetpasswordComponent } from './components/resetpassword/resetpassword.component';
import { AppRoutingModule } from './routing//app-routing.module';
import { MyNavComponent } from './components/my-nav/my-nav.component';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule, MatButtonModule, MatSidenavModule, MatIconModule, MatListModule, MatGridListModule, MatCardModule, MatMenuModule, MatTableModule, MatPaginatorModule, MatSortModule } from '@angular/material';
import { AlertComponent } from './components/alert/alert.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ProfileComponent } from './components/profile/profile.component';
import { AuthenticationService } from './services/authentication.service';
/* Angular Flex Layout */
import { FlexLayoutModule } from "@angular/flex-layout";
import { NoteComponent } from './components/note/note.component';
import { LabelComponent } from './components/label/label.component';
import { ReminderComponent } from './components/reminder/reminder.component';
import { ArchiveComponent } from './components/archive/archive.component';
import { DisplaynotesComponent } from './components/displaynotes/displaynotes.component';
import { NotedataComponent } from './components/notedata/notedata.component';
import { TrashComponent } from './components/trash/trash.component';
import { NoteDialogComponent } from './components/note-dialog/note-dialog.component';
import { IconComponent } from './components/icon/icon.component';
import { SharedService } from './/services/shared.service';
import { DataService } from './/services/data.service';
// import { TokenInterceptorService } from './services/token-interceptor.service';



@NgModule({
  declarations: [
    // SharedService,
    AppComponent,
    LoginComponent,
    RegisterComponent,
    ForgotpasswordComponent,
    ResetpasswordComponent,
    MyNavComponent,
    AlertComponent,
    ProfileComponent,
    NoteComponent,
    LabelComponent,
    ReminderComponent,
    ArchiveComponent,
    DisplaynotesComponent,
    NotedataComponent,
    TrashComponent,
    NoteDialogComponent,
    IconComponent,

    // TokenInterceptorService,


  ],

  imports: [
    ReactiveFormsModule,
    BrowserModule,
    AppMaterialModule,
    BrowserAnimationsModule,
    FormsModule,
    HttpClientModule,
    RouterModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    LayoutModule,
    MatToolbarModule,
    MatButtonModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
    MatGridListModule,
    MatCardModule,
    MatMenuModule,
    MatTableModule,
    MatPaginatorModule,
    FormsModule,
    ReactiveFormsModule,
    FlexLayoutModule,
   

  ],


  providers: [
    // { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptorService, multi: true },
    UserService,AuthGuard,AlertService,AuthenticationService,SharedService,DataService
    ],
  bootstrap: [AppComponent],
  entryComponents: [NoteDialogComponent]
})


export class AppModule { }
