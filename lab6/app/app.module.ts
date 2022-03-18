import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { ShareButtonsModule } from 'ngx-sharebuttons/buttons';
import { ShareIconsModule } from 'ngx-sharebuttons/icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { ProductListComponent } from './product-list/product-list.component';
import { ProductItemComponent } from './product-item/product-item.component';
import { ShareModule } from 'ngx-sharebuttons';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AlbumComponent } from './album/album.component';
import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { AlbumDetailComponent } from './album-detail/album-detail.component';
import { AlbumPhotosComponent } from './album-photos/album-photos.component';
import { FormsModule } from '@angular/forms';

const appRoutes: Routes = [
  { path: 'l1', component: AppComponent },
  {path: 'album', component: AlbumComponent},
  {path:'album/:id', component: AlbumDetailComponent},
  {path:'album/:id/photos', component: AlbumPhotosComponent}
];
@NgModule({
  declarations: [
    AppComponent,
    ProductListComponent,
    ProductItemComponent,
    AlbumComponent,
    HomeComponent,
    AboutComponent,
    AlbumDetailComponent,
    AlbumPhotosComponent,
  ],
  imports: [
    NgbModule,
    FormsModule,
    BrowserModule,
    FontAwesomeModule,
    ShareModule,
    ShareButtonsModule,
    ShareIconsModule,
    RouterModule.forRoot(
      appRoutes,
      { enableTracing: true } // <-- debugging purposes only
    )
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
 }
