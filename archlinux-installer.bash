# write an arch linux installation script

#!/bin/bash

#update system clock
timedatectl set-ntp true

#partition the disks
fdisk /dev/sda

#format the partitions
mkfs.ext4 /dev/sda1
mkfs.ext4 /dev/sda2

#mount the file systems
mount /dev/sda1 /mnt
mkdir /mnt/home
mount /dev/sda2 /mnt/home

#select the mirrors
pacman -Sy
pacman -S reflector
reflector --latest 20 --protocol https --sort rate --save /etc/pacman.d/mirrorlist

#install the base packages
pacstrap /mnt base base-devel

#generate the fstab file
genfstab -U -p /mnt >> /mnt/etc/fstab

#change root into the new system
arch-chroot /mnt

#set the time zone
ln -sf /usr/share/zoneinfo/America/New_York /etc/localtime

#set the hardware clock
hwclock --systohc

#uncomment en_US.UTF-8 UTF-8 and other needed localizations in /etc/locale.gen, and generate them with
locale-gen

#set the system locale
echo LANG=en_US.UTF-8 > /etc/locale.conf

#set the hostname
echo archlinux > /etc/hostname

#add matching entries to hosts file
echo 127.0.0.1 localhost >> /etc/hosts
echo ::1 localhost >> /etc/hosts
echo 127.0.1.1 archlinux.localdomain archlinux >> /etc/hosts

#install and configure bootloader
pacman -S grub efibootmgr
grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub
grub-mkconfig -o /boot/grub/grub.cfg

#set root password
passwd

#exit chroot
exit

#umount file systems
umount -R /mnt
reboot