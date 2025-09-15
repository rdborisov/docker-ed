Vagrant.configure("2") do |config|
    cpu_cap = ENV.has_key?('SRV_CPU_CAP') ? ENV['SRV_CPU_CAP'] : 100
    cpu_num = ENV.has_key?('SRV_CPU_NUM') ? ENV['SRV_CPU_NUM'] : 2
    mem_lim = ENV.has_key?('SRV_MEM_LIM') ? ENV['SRV_MEM_LIM'] : 1536
  
    (1..1).each do |i|
      config.vm.define "server_#{i}" do |server|
        server.vm.box = "ubuntu/focal64"
        server.vm.provider "virtualbox" do |v|
          v.customize ["modifyvm", :id, "--cpuexecutioncap", cpu_cap]
          v.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/vagrant", "1"]
        end
        server.vm.hostname = "server.localhost"
        server.vm.network "private_network", ip: "192.168.99.10#{i}"
        server.vm.synced_folder ".", "/home/vagrant/host", disabled: true
        server.vm.synced_folder ".", "/home/vagrant/host", :mount_options => [
          "dmode=777","fmode=777"
        ], type: "virtualbox"
        server.vm.provision :shell, inline: "sudo chmod +x /home/vagrant/host/docker-install.sh && sudo bash /home/vagrant/host/docker-install.sh -y"
        server.vm.provision :shell, inline: "cd /home/vagrant/host/docker-ed &&docker build -t app . && docker image ls -a"
        server.vm.provision :shell, inline: "docker run -d --rm -p 2000:8000 --name app app"
        server.vm.provider "virtualbox" do |v|
          v.memory = mem_lim
          v.cpus = cpu_num
        end
      end
    end
  end
  